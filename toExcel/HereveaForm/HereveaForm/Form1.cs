using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Windows.Forms;
using Herevea.Reports;
using Microsoft.Office.Interop.Excel;
using Microsoft.Reporting.WinForms;
using Application = System.Windows.Forms.Application;
using Newtonsoft.Json;

namespace HereveaForm
{
    public partial class Form1 : Form
    {
        private BackgroundWorker worker = new BackgroundWorker();
        private Microsoft.Office.Interop.Excel.Application xlApp = null;
        private Workbook wb = null;
        private Image image;
        private int angle = 0;
        private string path;
        private readonly ReportCreator _reportCreator;

        public Form1()
        {
            InitializeComponent();
            path = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            image = Image.FromFile(Path.Combine(path, "huellaPie.png"));
            pictureBox1.Image = image;

            worker.DoWork += (sender, args) => Interop();
            worker.WorkerReportsProgress = true;
            worker.ProgressChanged += worker_ProgressChanged;
            worker.RunWorkerAsync();
        }


        void worker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            this.progressBar1.Value = e.ProgressPercentage;
        }

        private void Interop()
        {
            try
            {
                Trace.TraceInformation("Calculando huella...");
                File.Delete(Path.Combine(path, "result.txt"));
                var data = File.ReadAllText(Path.Combine(path, "data.txt"));
                dynamic dataObj = JsonConvert.DeserializeObject(data);

                var file = new FileInfo(Path.Combine(path, "Huella.xls"));
                xlApp = new Microsoft.Office.Interop.Excel.Application { Visible = false, DisplayAlerts = false };
                wb = xlApp.Workbooks.Open(file.FullName);
                worker.ReportProgress(25);
                Console.WriteLine("Calculando huella total...");

                var sheet = (Worksheet) wb.Sheets["Características_proyectos"];
                var project = CalculateProject(dataObj, sheet);

                sheet = (Worksheet) wb.Sheets["Seleccion proyecto HEREVEA02"];
                var sheetDespl = (Worksheet)wb.Sheets["Datos aux_desplegables"];
                
                worker.ReportProgress(50);

                InsertData(sheet, project, dataObj);

                var sheetHuella = (Worksheet) wb.Sheets["HE Total"];
                var sheetPEM = (Worksheet) wb.Sheets["PEM Proyecto"];
                sheetPEM.Calculate();
                sheetHuella.Calculate();
                
                worker.ReportProgress(75);
                try
                {
                    wb.Save();
                }
                catch (Exception ex)
                {
                    Trace.TraceError("Error intentando guardar excel: " + ex);
                }
                
                var reportFileName = string.Format("{0}_{1}", dataObj.RefCatastral, DateTime.Now.Ticks%1000000);
                var reportDirectory = Path.Combine(Path.GetDirectoryName(path), "Informes");
                if (!Directory.Exists(reportDirectory))
                    Directory.CreateDirectory(reportDirectory);
                var reportPath = Path.Combine(reportDirectory, reportFileName);

                var result = GetResults(sheetHuella, sheetPEM);

                var reportCreator = new ReportCreator(path, reportPath, dataObj, result, sheetDespl);
                reportPath = reportCreator.CreateReport();

                result.Add("ReportPath", reportPath);

                string resultJson = JsonConvert.SerializeObject(result);
                File.WriteAllText(Path.Combine(path, "result.txt"), resultJson);
                Console.WriteLine("Huella total: " + sheetHuella.Cells[49, 3].Value.ToString());
                
            }
            catch (Exception ex)
            {
                Trace.TraceError("Error:" + ex);
            }
            finally
            {
                worker.ReportProgress(100);
                Application.Exit();    
            }
        }

        private static void InsertData(Worksheet sheet, dynamic project, dynamic dataObj)
        {
            sheet.Cells[6, 12].Value = project;
            Console.WriteLine("Proyecto: " + project);

            sheet.Cells[8, 12].Value = dataObj.Superficie;
            
            sheet.Cells[14, 7].Value = dataObj.Pilotes;
            sheet.Cells[14, 8].Value = dataObj.PilotesAct;
            sheet.Cells[16, 7].Value = dataObj.Arquetas;
            sheet.Cells[16, 8].Value = dataObj.ArquetasAct;
            sheet.Cells[17, 7].Value = dataObj.Colectores;
            sheet.Cells[17, 8].Value = dataObj.ColectoresAct;
            sheet.Cells[18, 7].Value = dataObj.Bajantes;
            sheet.Cells[18, 8].Value = dataObj.BajantesAct;
            sheet.Cells[21, 7].Value = dataObj.Forjados;
            sheet.Cells[21, 8].Value = dataObj.ForjadosAct;
            sheet.Cells[27, 7].Value = dataObj.Fisuras;
            sheet.Cells[27, 8].Value = dataObj.FisurasAct;
            sheet.Cells[28, 7].Value = dataObj.Grietas;
            sheet.Cells[28, 8].Value = dataObj.GrietasAct;
            sheet.Cells[30, 7].Value = dataObj.LadFisuras;
            sheet.Cells[30, 8].Value = dataObj.LadFisurasAct;
            sheet.Cells[31, 7].Value = dataObj.LadGrietas;
            sheet.Cells[31, 8].Value = dataObj.LadGrietasAct;
            sheet.Cells[32, 7].Value = dataObj.LadHumSuelo;
            sheet.Cells[32, 8].Value = dataObj.LadHumSueloAct;
            sheet.Cells[33, 7].Value = dataObj.LadHumTecho;
            sheet.Cells[33, 8].Value = dataObj.LadHumTechoAct;
            sheet.Cells[35, 7].Value = dataObj.IntFisuras;
            sheet.Cells[35, 8].Value = dataObj.IntFisurasAct;
            sheet.Cells[36, 7].Value = dataObj.IntGrietas;
            sheet.Cells[36, 8].Value = dataObj.IntGrietasAct;
            sheet.Cells[37, 7].Value = dataObj.HumSuelo;
            sheet.Cells[37, 8].Value = dataObj.HumSueloAct;
            sheet.Cells[40, 7].Value = dataObj.CubHorCom;
            sheet.Cells[40, 8].Value = dataObj.CubHorComAct;
            sheet.Cells[41, 7].Value = dataObj.CubHorFaldon;
            sheet.Cells[41, 8].Value = dataObj.CubHorFaldonAct;
            sheet.Cells[42, 7].Value = dataObj.CubHorEncParamVer;
            sheet.Cells[42, 8].Value = dataObj.CubHorEncParamVerAct;
            sheet.Cells[43, 7].Value = dataObj.CubHorEncCazoletas;
            sheet.Cells[43, 8].Value = dataObj.CubHorEncCazoletasAct;
            sheet.Cells[45, 7].Value = dataObj.CubIncCompleta;
            sheet.Cells[45, 8].Value = dataObj.CubIncCompletaAct;
            sheet.Cells[46, 7].Value = dataObj.CubIncFaldon;
            sheet.Cells[46, 8].Value = dataObj.CubIncFaldonAct;
            sheet.Cells[47, 7].Value = dataObj.CubIncRemates;
            sheet.Cells[47, 8].Value = dataObj.CubIncRematesAct;
            sheet.Cells[48, 7].Value = dataObj.CubIncEncParamVer;
            sheet.Cells[48, 8].Value = dataObj.CubIncEncParamVerAct;

            sheet.Cells[50, 7].Value = dataObj.Climatizacion;
            sheet.Cells[50, 8].Value = dataObj.ClimatizacionAct;
            sheet.Cells[51, 7].Value = dataObj.Radiadores;
            sheet.Cells[51, 8].Value = dataObj.RadiadoresAct;
            sheet.Cells[52, 7].Value = dataObj.Circuitos;
            sheet.Cells[52, 8].Value = dataObj.CircuitosAct;
            sheet.Cells[53, 7].Value = dataObj.LineasYDerivaciones;
            sheet.Cells[53, 8].Value = dataObj.LineasYDerivacionesAct;
            sheet.Cells[54, 7].Value = dataObj.PuntosLuz;
            sheet.Cells[54, 8].Value = dataObj.PuntosLuzAct;
            sheet.Cells[55, 7].Value = dataObj.TomaCorriente;
            sheet.Cells[55, 8].Value = dataObj.TomaCorrienteAct;
            sheet.Cells[56, 7].Value = dataObj.ConductorPuestaTierra;
            sheet.Cells[56, 8].Value = dataObj.ConductorPuestaTierraAct;
            sheet.Cells[57, 7].Value = dataObj.Canalizaciones;
            sheet.Cells[57, 8].Value = dataObj.CanalizacionesAct;
            sheet.Cells[58, 7].Value = dataObj.Desagues;
            sheet.Cells[58, 8].Value = dataObj.DesaguesAct;
            sheet.Cells[59, 7].Value = dataObj.CanalizacionesAguaFria;
            sheet.Cells[59, 8].Value = dataObj.CanalizacionesAguaFriaAct;
            sheet.Cells[60, 7].Value = dataObj.Sanitarios;
            sheet.Cells[60, 8].Value = dataObj.SanitariosAct;
            sheet.Cells[61, 7].Value = dataObj.Termos;
            sheet.Cells[61, 8].Value = dataObj.TermosAct;
            
            sheet.Cells[63, 7].Value = dataObj.CarpLigera;
            sheet.Cells[63, 8].Value = dataObj.CarpLigeraAct;
            sheet.Cells[64, 7].Value = dataObj.CarpMadera;
            sheet.Cells[64, 8].Value = dataObj.CarpMaderaAct;
            sheet.Cells[66, 7].Value = dataObj.Rejas;
            sheet.Cells[66, 8].Value = dataObj.RejasAct;
            
            sheet.Cells[69, 7].Value = dataObj.Escalera;
            sheet.Cells[69, 5].Value = dataObj.EscaleraAct;
            sheet.Cells[70, 7].Value = dataObj.Rampa;
            sheet.Cells[70, 5].Value = dataObj.RampaAct;
            sheet.Cells[71, 7].Value = dataObj.Portero;
            sheet.Cells[71, 5].Value = dataObj.PorteroAct;
            sheet.Cells[72, 7].Value = dataObj.Ascensores;
            sheet.Cells[16, 12].Value = dataObj.AscensoresAct;
        }

        private static Dictionary<string, object> GetResults(Worksheet sheetHuella, Worksheet sheetPEM)
        {
            return new Dictionary<string, object>()
            {
                {"Total", sheetHuella.Cells[56, 3].Value ?? 0M},
                {"Energia", sheetHuella.Cells[54, 3].Value ?? 0M},
                {"Bosques", sheetHuella.Cells[54, 4].Value ?? 0M},
                {"Pastos", sheetHuella.Cells[54, 5].Value ?? 0M},
                {"Mar", sheetHuella.Cells[54, 6].Value ?? 0M},
                {"Cultivos", sheetHuella.Cells[54, 7].Value ?? 0M},
                {"SuperficieConsumida", sheetHuella.Cells[54, 8].Value ?? 0M},

                {"Maquinaria", sheetHuella.Cells[44,3].Value ?? 0},
                {"Electricidad", sheetHuella.Cells[45,3].Value ?? 0},
                {"Agua", sheetHuella.Cells[46,3].Value ?? 0},
                {"Alimentos", sheetHuella.Cells[47,3].Value ?? 0},
                {"Movilidad", sheetHuella.Cells[48,3].Value ?? 0},
                {"Residuos RSU", sheetHuella.Cells[49,3].Value ?? 0},
                {"Materiales", sheetHuella.Cells[50,3].Value ?? 0},
                {"Residuos RCD", sheetHuella.Cells[51,3].Value ?? 0},

                {"MaqEn", sheetHuella.Cells[44,3].Value},
                {"EleEn", sheetHuella.Cells[45,3].Value},
                {"AgBo", sheetHuella.Cells[46,4].Value},
                {"AliEn", sheetHuella.Cells[47,3].Value},
                {"AliPa", sheetHuella.Cells[47,5].Value},
                {"AliMa", sheetHuella.Cells[47,6].Value},
                {"AliCu", sheetHuella.Cells[47,7].Value},
                {"MovEn", sheetHuella.Cells[48,3].Value},
                {"RsuEn", sheetHuella.Cells[49,3].Value},
                {"MatEn", sheetHuella.Cells[50,3].Value},
                {"RcdEn", sheetHuella.Cells[51,3].Value},
                {"OcuSu", sheetHuella.Cells[52,8].Value},

                {"Cimentaciones", sheetPEM.Cells[67, 7].Value ?? 0},
                {"Saneamiento",   sheetPEM.Cells[68, 7].Value ?? 0},
                {"Estructuras",   sheetPEM.Cells[69, 7].Value ?? 0},
                {"Albañileria",   sheetPEM.Cells[70, 7].Value ?? 0},
                {"Cubiertas",     sheetPEM.Cells[71, 7].Value ?? 0},
                {"Instalaciones", sheetPEM.Cells[72, 7].Value ?? 0},
                {"Carpinteria",   sheetPEM.Cells[73, 7].Value ?? 0},
                {"Accesibilidad", sheetPEM.Cells[74, 7].Value ?? 0},
                {"Residuos",      sheetPEM.Cells[75, 7].Value ?? 0},
                    
                {"Rehabilitacion", sheetPEM.Cells[77, 7].Value ?? 0},
                    
                {"DemolicionEdificio", sheetPEM.Cells[94, 7].Value ?? 0},
                {"DemolicionResiduos", sheetPEM.Cells[95, 7].Value ?? 0},

                {"Demolicion", sheetPEM.Cells[97, 7].Value ?? 0},
                {"Construccion", sheetPEM.Cells[108, 7].Value ?? 0},
                {"HEDemolicion", sheetHuella.Cells[75, 4].Value ?? 0},
                {"HEConstruccion", sheetHuella.Cells[81, 4].Value ?? 0},
            };
        }

        private string CalculateProject(dynamic dataObj, Worksheet sheet)
        {
            var matchCaracteristicas = new Dictionary<int, int>();
            for (int i = 3; i < 99; i++)
            {
                matchCaracteristicas[i] = 0;
                if (dataObj.PlantasSobre != null && sheet.Cells[i, 2].Value != null &&
                    PlantasEqual(dataObj.PlantasSobre.ToString(), sheet.Cells[i, 2].Value.ToString()))
                {
                    matchCaracteristicas[i]++;
                }
                if (dataObj.PlantasBajo != null && sheet.Cells[i, 3].Value != null &&
                    PlantasEqual(dataObj.PlantasBajo.ToString(), sheet.Cells[i, 3].Value.ToString()))
                {
                    matchCaracteristicas[i]++;
                }
                if (dataObj.PlantaBajaViviendas != null &&
                    (sheet.Cells[i, 7].Value == null && dataObj.PlantaBajaViviendas.ToString().Equals("no", StringComparison.InvariantCultureIgnoreCase)
                    || (sheet.Cells[i, 7].Value != null && dataObj.PlantaBajaViviendas.ToString().Equals(sheet.Cells[i, 7].Value.ToString(), StringComparison.InvariantCultureIgnoreCase))))
                {
                    matchCaracteristicas[i]++;
                }
                if (dataObj.Cimentacion != null && sheet.Cells[i, 8].Value != null &&
                    dataObj.Cimentacion.ToString().Equals(sheet.Cells[i, 8].Value.ToString(), StringComparison.InvariantCultureIgnoreCase))
                {
                    matchCaracteristicas[i]++;
                }
                if (dataObj.Estructura != null && sheet.Cells[i, 9].Value != null &&
                    dataObj.Estructura.ToString().Equals(sheet.Cells[i, 9].Value.ToString(), StringComparison.InvariantCultureIgnoreCase))
                {
                    matchCaracteristicas[i]++;
                }
                if (dataObj.Cubierta != null && sheet.Cells[i, 10].Value != null &&
                    dataObj.Cubierta.ToString().Equals(sheet.Cells[i, 10].Value.ToString(), StringComparison.InvariantCultureIgnoreCase))
                {
                    matchCaracteristicas[i]++;
                }
            }
            var projectIndex = matchCaracteristicas.Aggregate((l, r) => l.Value > r.Value ? l : r).Key;
            return string.Format("c{0}", sheet.Cells[projectIndex, 1].Value.ToString().Trim('*'));
        }

        private bool PlantasEqual(string plantasSobre, string excelValue)
        {
            if (excelValue.Contains(plantasSobre))
            {
                return true;
            }
            if (Convert.ToInt32(plantasSobre) > 5 && excelValue.Equals("más de 5 plantas", StringComparison.InvariantCultureIgnoreCase))
            {
                return true;
            }
            return false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            image = RotateImage(image);
            pictureBox1.Image = image;
        }

        public Image RotateImage(Image img)
        {
            var bmp = new Bitmap(img);

            using (Graphics gfx = Graphics.FromImage(bmp))
            {
                gfx.Clear(Color.Transparent);
                gfx.DrawImage(img, 0, 0, img.Width, img.Height);
            }

            bmp.RotateFlip(RotateFlipType.Rotate270FlipNone);
            return bmp;
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (wb != null)
            {
                wb.Close(false);
                xlApp.Quit();
            }
        }
    }
}
