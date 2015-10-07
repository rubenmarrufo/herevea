using System;
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
        private readonly string _reportPath;
        private readonly dynamic _data;
        private readonly Dictionary<string, object> _result;

        public ReportCreator(string path, dynamic data)
        {
            _path = path;
            _data = data;
        }

        public ReportCreator(string path, string reportPath, dynamic dataObj, Dictionary<string, object> result)
        {
            _path = path;
            _reportPath = reportPath;
            _data = dataObj;
            _result = result;
        }

        public string CreateReport()
        {
            var dataSets = GetDataSets();

            return GenerateReport(dataSets);
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
            var reportDto = new List<HuellaReportDTO>
            {
                new HuellaReportDTO
                {
                    Provincia = _data.Provincia,
                    Municipio = _data.Municipio,
                    Direccion = _data.Direccion,
                    RefCatastral = _data.RefCatastral,
                    HuellaConstruccionSuperficie = SafeToDecimal(_result["HEConstruccion"]),
                    HuellaConstruccion = SafeToDecimal(_result["HEConstruccion"]) * SafeToDecimal(_data.Superficie),
                    HuellaDemolicionSuperficie = SafeToDecimal(_result["HEDemolicion"]),
                    HuellaDemolicion = SafeToDecimal(_result["HEDemolicion"]) * SafeToDecimal(_data.Superficie),
                    HuellaTotalSuperficie = SafeToDecimal(_result["Total"]),
                    HuellaTotal = SafeToDecimal(_result["Total"]) * SafeToDecimal(_data.Superficie),
                    MaqEn = SafeToDecimal(_result["MaqEn"]),
                    EleEn = SafeToDecimal(_result["EleEn"]),
                    AgBo =  SafeToDecimal(_result["AgBo"] ),
                    AliEn = SafeToDecimal(_result["AliEn"]),
                    AliPa = SafeToDecimal(_result["AliPa"]),
                    AliMa = SafeToDecimal(_result["AliMa"]),
                    AliCu = SafeToDecimal(_result["AliCu"]),
                    MovEn = SafeToDecimal(_result["MovEn"]),
                    RsuEn = SafeToDecimal(_result["RsuEn"]),
                    MatEn = SafeToDecimal(_result["MatEn"]),
                    RcdEn = SafeToDecimal(_result["RcdEn"]),
                    OcuSu = SafeToDecimal(_result["OcuSu"]),

                    HEEnSuperficie = SafeToDecimal(_result["Energia"]),
                    HEBoSuperficie = SafeToDecimal(_result["Bosques"]),
                    HEPaSuperficie = SafeToDecimal(_result["Pastos"]),
                    HECuSuperficie = SafeToDecimal(_result["Cultivos"]),
                    HEMaSuperficie = SafeToDecimal(_result["Mar"]),
                    HESuSuperficie = SafeToDecimal(_result["SuperficieConsumida"]),

                    HEEn = SafeToDecimal(_result["Energia"]) * SafeToDecimal(_data.Superficie),
                    HEBo = SafeToDecimal(_result["Bosques"])* SafeToDecimal(_data.Superficie),
                    HEPa = SafeToDecimal(_result["Pastos"])* SafeToDecimal(_data.Superficie),
                    HECu = SafeToDecimal(_result["Cultivos"])* SafeToDecimal(_data.Superficie),
                    HEMa = SafeToDecimal(_result["Mar"])* SafeToDecimal(_data.Superficie),
                    HESu = SafeToDecimal(_result["SuperficieConsumida"])* SafeToDecimal(_data.Superficie),

                    NumeroPlantas = SafeToInt(_data.PlantasSobre),
                    AlturaEdificio = SafeToDecimal(_data.Altura),
                    Superficie = SafeToDecimal(_data.Superficie),
                }
            };

            var energiaTotal = SafeToDecimal(_result["Maquinaria"]) + SafeToDecimal(_result["Electricidad"]) +
                               SafeToDecimal(_result["Agua"]) +
                               SafeToDecimal(_result["Alimentos"]) + SafeToDecimal(_result["Movilidad"]) +
                               SafeToDecimal(_result["Residuos RSU"]) + SafeToDecimal(_result["Materiales"]) +
                               SafeToDecimal(_result["Residuos RCD"]);
            var energias = new List<Energias>
            {
                new Energias {Categoria = "Maquinaria", Impacto = SafeToDecimal(_result["Maquinaria"])/energiaTotal},
                new Energias {Categoria = "Electricidad", Impacto = SafeToDecimal(_result["Electricidad"])/energiaTotal},
                new Energias {Categoria = "Agua", Impacto = SafeToDecimal(_result["Agua"])/energiaTotal},
                new Energias {Categoria = "Alimentos", Impacto = SafeToDecimal(_result["Alimentos"])/energiaTotal},
                new Energias {Categoria = "Movilidad", Impacto = SafeToDecimal(_result["Movilidad"])/energiaTotal},
                new Energias {Categoria = "Residuos RSU", Impacto = SafeToDecimal(_result["Residuos RSU"])/energiaTotal},
                new Energias {Categoria = "Materiales", Impacto = SafeToDecimal(_result["Materiales"])/energiaTotal},
                new Energias {Categoria = "Residuos RCD", Impacto = SafeToDecimal(_result["Residuos RCD"])/energiaTotal}
            };
            var heParcial = new List<HEParcial>
            {
                new HEParcial {Categoria = "Energía", Valor = SafeToDecimal(_result["Energia"])},
                new HEParcial {Categoria = "Bosques", Valor = SafeToDecimal(_result["Bosques"])},
                new HEParcial {Categoria = "Pastos", Valor = SafeToDecimal(_result["Pastos"])},
                new HEParcial {Categoria = "Mar", Valor = SafeToDecimal(_result["Mar"])},
                new HEParcial {Categoria = "Cultivos", Valor = SafeToDecimal(_result["Cultivos"])},
                new HEParcial {Categoria = "Superficie Consumida", Valor = SafeToDecimal(_result["SuperficieConsumida"])},
            };
            var pem = new List<PEM>
            {
                new PEM()
                {
                    Cimentaciones = SafeToDecimal(_result["Cimentaciones"]),
                    Saneamiento = SafeToDecimal(_result["Saneamiento"]),  
                    Estructuras = SafeToDecimal(_result["Estructuras"]),  
                    Albañileria = SafeToDecimal(_result["Albañileria"]),  
                    Cubiertas = SafeToDecimal(_result["Cubiertas"]),   
                    Instalaciones = SafeToDecimal(_result["Instalaciones"]),
                    Carpinteria = SafeToDecimal(_result["Carpinteria"]),
                    Accesibilidad = SafeToDecimal(_result["Accesibilidad"]),
                    Residuos = SafeToDecimal(_result["Residuos"]),

                    Rehabilitacion = SafeToDecimal(_result["Rehabilitacion"]),
                    DemolicionEdificio = SafeToDecimal(_result["DemolicionEdificio"]),
                    DemolicionResiduos = SafeToDecimal(_result["DemolicionResiduos"]),
                    Construccion = SafeToDecimal(_result["Construccion"]),
                }
            };

            return new Dictionary<string, IEnumerable>
            {
                {"DataSet1", reportDto},
                {"DataSet2", energias},
                {"DataSet3", heParcial},
                {"DataSet4", actuaciones},
                {"DataSet5", pem}
            };
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

        private string GenerateReport(Dictionary<string,IEnumerable> dataSets)
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

            var saveAs = string.Format("{0}.pdf", _reportPath);

            var idx = 0;
            while (File.Exists(_reportPath))
            {
                idx++;
                saveAs = string.Format("{0}.{1}.pdf", _reportPath, idx);
            }

            using (var stream = new FileStream(saveAs, FileMode.Create, FileAccess.Write))
            {
                stream.Write(renderedBytes, 0, renderedBytes.Length);
                stream.Close();
            }

            lr.Dispose();
            return Path.GetFileName(saveAs);
        }

        public static decimal SafeToDecimal(object o)
        {
            try
            {
                return Convert.ToDecimal(o);
            }
            catch (Exception)
            {
                return 0M;
            }
        }

        private int SafeToInt(object o)
        {
            try
            {
                return Convert.ToInt32(o);
            }
            catch (Exception)
            {
                return 0;
            }
        }
    }
}