using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Office.Interop.Excel;
using Newtonsoft.Json;
using Application = System.Windows.Forms.Application;

namespace HereveaForm
{
    public partial class Form1 : Form
    {
        BackgroundWorker worker = new BackgroundWorker();

        public Form1()
        {
            InitializeComponent();
            worker.DoWork += (sender,args) => Interop();
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
            var path = Assembly.GetExecutingAssembly().Location;
            var xlApp = new Microsoft.Office.Interop.Excel.Application { Visible = false };
            var file = new FileInfo(Path.Combine(Path.GetDirectoryName(path), "Huella.xlsx"));
            var wb = xlApp.Workbooks.Open(file.FullName);
            worker.ReportProgress(25);
            Console.WriteLine("Calculando huella total...");

            var data = File.ReadAllText(Path.Combine(Path.GetDirectoryName(path), "data.txt"));
            dynamic dataObj = JsonConvert.DeserializeObject(data);

            var sheet = (Worksheet) wb.Sheets["Características_proyectos"];
            var project = CalculateProject(dataObj, sheet);

            sheet = (Worksheet) wb.Sheets["Seleccion proyecto HEREVEA02"];
            worker.ReportProgress(50);

            sheet.Cells[6, 12].Value = project;

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
            sheet.Cells[41, 7].Value = dataObj.CubHorCom;
            sheet.Cells[41, 8].Value = dataObj.CubHorComAct;
            sheet.Cells[42, 7].Value = dataObj.CubHorFaldon;
            sheet.Cells[42, 8].Value = dataObj.CubHorFaldonAct;
            sheet.Cells[43, 7].Value = dataObj.CubHorEncParamVer;
            sheet.Cells[43, 8].Value = dataObj.CubHorEncParamVerAct;
            sheet.Cells[44, 7].Value = dataObj.CubHorEncCazoletas;
            sheet.Cells[44, 8].Value = dataObj.CubHorEncCazoletasAct;
            sheet.Cells[46, 7].Value = dataObj.CubIncCompleta;
            sheet.Cells[46, 8].Value = dataObj.CubIncCompletaAct;
            sheet.Cells[47, 7].Value = dataObj.CubIncFaldon;
            sheet.Cells[47, 8].Value = dataObj.CubIncFaldonAct;
            sheet.Cells[48, 7].Value = dataObj.CubIncRemates;
            sheet.Cells[48, 8].Value = dataObj.CubIncRematesAct;
            sheet.Cells[49, 7].Value = dataObj.CubIncEncParamVer;
            sheet.Cells[49, 8].Value = dataObj.CubIncEncParamVerAct;
            sheet.Cells[51, 7].Value = dataObj.Climatizacion;
            sheet.Cells[51, 8].Value = dataObj.ClimatizacionAct;
            sheet.Cells[52, 7].Value = dataObj.Conductos;
            sheet.Cells[52, 8].Value = dataObj.ConductosAct;
            sheet.Cells[53, 7].Value = dataObj.Radiadores;
            sheet.Cells[53, 8].Value = dataObj.RadiadoresAct;
            sheet.Cells[54, 7].Value = dataObj.Circuitos;
            sheet.Cells[54, 8].Value = dataObj.CircuitosAct;
            sheet.Cells[55, 7].Value = dataObj.LineasYDerivaciones;
            sheet.Cells[55, 8].Value = dataObj.LineasYDerivacionesAct;
            sheet.Cells[56, 7].Value = dataObj.PuntosLuz;
            sheet.Cells[56, 8].Value = dataObj.PuntosLuzAct;
            sheet.Cells[57, 7].Value = dataObj.TomaCorriente;
            sheet.Cells[57, 8].Value = dataObj.TomaCorrienteAct;
            sheet.Cells[58, 7].Value = dataObj.ConductorPuestaTierra;
            sheet.Cells[58, 8].Value = dataObj.ConductorPuestaTierraAct;
            sheet.Cells[59, 7].Value = dataObj.Canalizaciones;
            sheet.Cells[59, 8].Value = dataObj.CanalizacionesAct;
            sheet.Cells[60, 7].Value = dataObj.Desagues;
            sheet.Cells[60, 8].Value = dataObj.DesaguesAct;
            sheet.Cells[61, 7].Value = dataObj.CanalizacionesAguaFria;
            sheet.Cells[61, 8].Value = dataObj.CanalizacionesAguaFriaAct;
            sheet.Cells[62, 7].Value = dataObj.Griferia;
            sheet.Cells[62, 8].Value = dataObj.GriferiaAct;
            sheet.Cells[63, 7].Value = dataObj.Sanitarios;
            sheet.Cells[63, 8].Value = dataObj.SanitariosAct;
            sheet.Cells[64, 7].Value = dataObj.Termos;
            sheet.Cells[64, 8].Value = dataObj.TermosAct;
            sheet.Cells[67, 7].Value = dataObj.CarpLigera;
            sheet.Cells[67, 8].Value = dataObj.CarpLigeraAct;
            sheet.Cells[68, 7].Value = dataObj.CarpMadera;
            sheet.Cells[68, 8].Value = dataObj.CarpMaderaAct;
            sheet.Cells[69, 7].Value = dataObj.Rejas;
            sheet.Cells[69, 8].Value = dataObj.RejasAct;
            sheet.Cells[65, 7].Value = dataObj.Ascensores;
            sheet.Cells[65, 8].Value = dataObj.AscensoresAct;

            var sheetHuella = (Worksheet)wb.Sheets["HE Total"];
            var sheetPEM = (Worksheet)wb.Sheets["PEM Proyecto"];
            sheetPEM.Calculate();
            sheetHuella.Calculate();
            worker.ReportProgress(75);
            var result = new Dictionary<string, object>()
            {
                {"Total", sheetHuella.Cells[49, 3].Value},
                {"Energia", sheetHuella.Cells[47, 3].Value},
                {"Bosques", sheetHuella.Cells[47, 4].Value},
                {"Pastos", sheetHuella.Cells[47, 5].Value},
                {"Mar", sheetHuella.Cells[47, 6].Value},
                {"Cultivos", sheetHuella.Cells[47, 7].Value},
                {"SuperficieConsumida", sheetHuella.Cells[47, 8].Value},
                {"Rehabilitacion", sheetPEM.Cells[58, 7].Value},
                {"Demolicion", sheetPEM.Cells[65, 7].Value},
                {"Construccion", sheetPEM.Cells[76, 6].Value}
            };
            
            string resultJson = JsonConvert.SerializeObject(result);
            File.WriteAllText(Path.Combine(Path.GetDirectoryName(path), "result.txt"), resultJson);
            Console.WriteLine("Huella total: " + sheet.Cells[47, 3].Value);

            wb.Close(true);
            xlApp.Quit();
            worker.ReportProgress(100);
            Application.Exit();
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
                if (dataObj.PlantaBajaViviendas != null && sheet.Cells[i, 7].Value != null && 
                    dataObj.PlantaBajaViviendas.ToString().Equals(sheet.Cells[i, 7].Value.ToString(), StringComparison.InvariantCultureIgnoreCase))
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
            return string.Format("c{0}",sheet.Cells[projectIndex, 1].Value.ToString().Trim('*'));
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
    }
}
