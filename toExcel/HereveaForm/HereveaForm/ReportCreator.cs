using System.Collections;
using System.Collections.Generic;
using System.IO;
using Herevea.Reports;
using Microsoft.Reporting.WinForms;

namespace HereveaForm
{
    public class ReportCreator
    {
        private readonly string _path;
        private readonly dynamic _data;

        public ReportCreator(string path, dynamic data)
        {
            _path = path;
            _data = data;
        }

        public void CreateReport()
        {
            var dataSets = GetTestDataSets();

            GenerateReport(dataSets);
        }

        private Dictionary<string, IEnumerable> GetDataSets()
        {
            var actuaciones = new List<Actuaciones>
            {
                new Actuaciones
                {
                    Pilotes = _data.Pilotes,
                    PilotesAct = _data.PilotesAct,
                    Arquetas = _data.Arquetas,
                    ArquetasAct = _data.ArquetasAct,
                    Colectores = _data.Colectores,
                    ColectoresAct = _data.ColectoresAct,
                    Bajantes = _data.Bajantes,
                    BajantesAct = _data.BajantesAct,
                    Forjados = _data.Forjados,
                    ForjadosAct = _data.ForjadosAct,
                    Fisuras = _data.Fisuras,
                    FisurasAct = _data.FisurasAct,
                    Grietas = _data.Grietas,
                    GrietasAct = _data.GrietasAct,
                    LadFisuras = _data.LadFisuras,
                    LadFisurasAct = _data.LadFisurasAct,
                    LadGrietas = _data.LadGrietas,
                    LadGrietasAct = _data.LadGrietasAct,
                    LadHumSuelo = _data.LadHumSuelo,
                    LadHumSueloAct = _data.LadHumSueloAct,
                    LadHumTecho = _data.LadHumTecho,
                    LadHumTechoAct = _data.LadHumTechoAct,
                    IntFisuras = _data.IntFisuras,
                    IntFisurasAct = _data.IntFisurasAct,
                    IntGrietas = _data.IntGrietas,
                    IntGrietasAct = _data.IntGrietasAct,
                    HumSuelo = _data.HumSuelo,
                    HumSueloAct = _data.HumSueloAct,
                    CubHorCom = _data.CubHorCom,
                    CubHorComAct = _data.CubHorComAct,
                    CubHorFaldon = _data.CubHorFaldon,
                    CubHorFaldonAct = _data.CubHorFaldonAct,
                    CubHorEncParamVer = _data.CubHorEncParamVer,
                    CubHorEncParamVerAct = _data.CubHorEncParamVerAct,
                    CubHorEncCazoletas = _data.CubHorEncCazoletas,
                    CubHorEncCazoletasAct = _data.CubHorEncCazoletasAct,
                    CubIncCompleta = _data.CubIncCompleta,
                    CubIncCompletaAct = _data.CubIncCompletaAct,
                    CubIncFaldon = _data.CubIncFaldon,
                    CubIncFaldonAct = _data.CubIncFaldonAct,
                    CubIncRemates = _data.CubIncRemates,
                    CubIncRematesAct = _data.CubIncRematesAct,
                    CubIncEncParamVer = _data.CubIncEncParamVer,
                    CubIncEncParamVerAct = _data.CubIncEncParamVerAct,
                    Climatizacion = _data.Climatizacion,
                    ClimatizacionAct = _data.ClimatizacionAct,
                    Radiadores = _data.Radiadores,
                    RadiadoresAct = _data.RadiadoresAct,
                    Circuitos = _data.Circuitos,
                    CircuitosAct = _data.CircuitosAct,
                    LineasYDerivaciones = _data.LineasYDerivaciones,
                    LineasYDerivacionesAct = _data.LineasYDerivacionesAct,
                    PuntosLuz = _data.PuntosLuz,
                    PuntosLuzAct = _data.PuntosLuzAct,
                    TomaCorriente = _data.TomaCorriente,
                    TomaCorrienteAct = _data.TomaCorrienteAct,
                    ConductorPuestaTierra = _data.ConductorPuestaTierra,
                    ConductorPuestaTierraAct = _data.ConductorPuestaTierraAct,
                    Canalizaciones = _data.Canalizaciones,
                    CanalizacionesAct = _data.CanalizacionesAct,
                    Desagues = _data.Desagues,
                    DesaguesAct = _data.DesaguesAct,
                    CanalizacionesAguaFria = _data.CanalizacionesAguaFria,
                    CanalizacionesAguaFriaAct = _data.CanalizacionesAguaFriaAct,
                    Termos = _data.Termos,
                    TermosAct = _data.TermosAct,
                    Sanitarios = _data.Sanitarios,
                    SanitariosAct = _data.SanitariosAct,
                    CarpLigera = _data.CarpLigera,
                    CarpLigeraAct = _data.CarpLigeraAct,
                    CarpMadera = _data.CarpMadera,
                    CarpMaderaAct = _data.CarpMaderaAct,
                    Rejas = _data.Rejas,
                    RejasAct = _data.RejasAct,
                    Escalera = _data.Escalera,
                    EscaleraAct = _data.EscaleraAct,
                    Rampa = _data.Rampa,
                    RampaAct = _data.RampaAct,
                    Portero = _data.Portero,
                    PorteroAct = _data.PorteroAct,
                    Ascensores = _data.Ascensores,
                    AscensoresAct = _data.AscensoresAct
                }
            };
            return new Dictionary<string, IEnumerable> {{"DataSet4", actuaciones}};
        }

        private static Dictionary<string, IEnumerable> GetTestDataSets()
        {
            var dataSource = new List<HuellaReportDTO>
            {
                new HuellaReportDTO()
                {
                    MaqEn = 333,
                    Superficie = 22.34M,
                    NumeroPlantas = 3,
                    AlturaEdificio = 33,
                    AliEn = 23.3M,
                    AgEn = 22.1M,
                    EleEn = 2.1M,
                    MatEn = 12,
                    MovEn = 5,
                    OcuEn = 22,
                    RcdEn = 12,
                    RsuEn = 7
                }
            };

            var energias = new List<Energias>()
            {
                new Energias()
                {
                    Impacto = 33,
                    Categoria = "Alimento"
                },
                new Energias()
                {
                    Impacto = 13,
                    Categoria = "Agua"
                },
                new Energias()
                {
                    Impacto = 5,
                    Categoria = "Movilidad"
                }
            };

            var heParcial = new List<HEParcial>()
            {
                new HEParcial()
                {
                    Valor = 33,
                    Categoria = "Energia"
                },
                new HEParcial()
                {
                    Valor = 13,
                    Categoria = "Bosques"
                },
                new HEParcial()
                {
                    Valor = 5,
                    Categoria = "Pastos"
                }
            };

            var actuaciones = new List<Actuaciones>()
            {
                new Actuaciones()
                {
                    Pilotes = "No hay actuaciones",
                    PilotesAct = "0"
                }
            };
            return new Dictionary<string, IEnumerable>()
            {
                {"DataSet1",dataSource},
                {"DataSet2",energias},
                {"DataSet3", heParcial},
                {"DataSet4",actuaciones}
            };
        }

        private void GenerateReport(Dictionary<string,IEnumerable> dataSets)
        {
            var lr = new LocalReport
            {
                ReportPath = Path.Combine(_path, "Report1.rdlc"),
                EnableExternalImages = true
            };

            foreach (var dataSet in dataSets)
            {
                lr.DataSources.Add(new ReportDataSource(dataSet.Key, dataSet.Value));
            }

            string mimeType, encoding, extension;

            Warning[] warnings;
            string[] streams;
            var renderedBytes = lr.Render
                (
                    "PDF",
                    @"<DeviceInfo><OutputFormat>PDF</OutputFormat><HumanReadablePDF>False</HumanReadablePDF></DeviceInfo>",
                    out mimeType,
                    out encoding,
                    out extension,
                    out streams,
                    out warnings
                );

            var saveAs = string.Format("{0}.pdf", Path.Combine(_path, "result"));

            var idx = 0;
            while (File.Exists(saveAs))
            {
                idx++;
                saveAs = string.Format("{0}.{1}.pdf", Path.Combine(_path, "myfilename"), idx);
            }

            using (var stream = new FileStream(saveAs, FileMode.Create, FileAccess.Write))
            {
                stream.Write(renderedBytes, 0, renderedBytes.Length);
                stream.Close();
            }

            lr.Dispose();
        }
    }
}