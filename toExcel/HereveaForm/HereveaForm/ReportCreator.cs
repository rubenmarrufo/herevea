using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using Herevea.Reports;
using Microsoft.Office.Interop.Excel;
using Microsoft.Reporting.WinForms;

namespace HereveaForm
{
    public class ReportCreator
    {
        private readonly string _path;
        private readonly string _reportPath;
        private readonly dynamic _data;
        private readonly Dictionary<string, object> _result;
        private readonly Worksheet _sheetDespl;

        public ReportCreator(string path, dynamic data)
        {
            _path = path;
            _data = data;
        }

        public ReportCreator(string path, string reportPath, dynamic dataObj, Dictionary<string, object> result, Worksheet sheetDespl)
        {
            _path = path;
            _reportPath = reportPath;
            _data = dataObj;
            _result = result;
            _sheetDespl = sheetDespl;
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
                    PilotesPUC = CalculatePUC(_data.Pilotes, "Cimentaciones"),
                    Arquetas = _data.Arquetas,
                    ArquetasAct = _data.ArquetasAct,
                    ArquetasPUC = CalculatePUC(_data.Arquetas, "Arquetas"),
                    Colectores = _data.Colectores,
                    ColectoresAct = _data.ColectoresAct,
                    ColectoresPUC = CalculatePUC(_data.Colectores, "Colectores"),
                    Bajantes = _data.Bajantes,
                    BajantesAct = _data.BajantesAct,
                    BajantesPUC = CalculatePUC(_data.Bajantes, "Bajantes"),
                    Forjados = _data.Forjados,
                    ForjadosAct = _data.ForjadosAct,
                    ForjadosPUC = CalculatePUC(_data.Forjados, "Forjados"),
                    Fisuras = _data.Fisuras,
                    FisurasAct = _data.FisurasAct,
                    FisurasPUC = CalculatePUC(_data.Fisuras, "Particiones"),
                    Grietas = _data.Grietas,
                    GrietasAct = _data.GrietasAct,
                    GrietasPUC = CalculatePUC(_data.Grietas, "Particiones"),
                    LadFisuras = _data.LadFisuras,
                    LadFisurasAct = _data.LadFisurasAct,
                    LadFisurasPUC = CalculatePUC(_data.LadFisuras, "Cerramientos"),
                    LadGrietas = _data.LadGrietas,
                    LadGrietasAct = _data.LadGrietasAct,
                    LadGrietasPUC = CalculatePUC(_data.LadGrietas, "Cerramientos"),
                    LadHumSuelo = _data.LadHumSuelo,
                    LadHumSueloAct = _data.LadHumSueloAct,
                    LadHumSueloPUC = CalculatePUC(_data.LadHumSuelo, "Cerramientos"),
                    LadHumTecho = _data.LadHumTecho,
                    LadHumTechoAct = _data.LadHumTechoAct,
                    LadHumTechoPUC = CalculatePUC(_data.LadHumTecho, "Cerramientos"),
                    IntFisuras = _data.IntFisuras,
                    IntFisurasAct = _data.IntFisurasAct,
                    IntFisurasPUC = CalculatePUC(_data.IntFisuras, "Fcas.interiores ladrillo"),
                    IntGrietas = _data.IntGrietas,
                    IntGrietasAct = _data.IntGrietasAct,
                    IntGrietasPUC = CalculatePUC(_data.IntGrietas, "Fcas.interiores ladrillo"),
                    HumSuelo = _data.HumSuelo,
                    HumSueloAct = _data.HumSueloAct,
                    HumSueloPUC = CalculatePUC(_data.HumSuelo, "Fcas.interiores ladrillo"),
                    CubHorCom = _data.CubHorCom,
                    CubHorComAct = _data.CubHorComAct,
                    CubHorComPUC = CalculatePUC(_data.CubHorCom, "Horizontal"),
                    CubHorFaldon = _data.CubHorFaldon,
                    CubHorFaldonAct = _data.CubHorFaldonAct,
                    CubHorFaldonPUC = CalculatePUC(_data.CubHorFaldon, "Horizontal"),
                    CubHorEncParamVer = _data.CubHorEncParamVer,
                    CubHorEncParamVerAct = _data.CubHorEncParamVerAct,
                    CubHorEncParamVerPUC = CalculatePUC(_data.CubHorEncParamVer, "Horizontal"),
                    CubHorEncCazoletas = _data.CubHorEncCazoletas,
                    CubHorEncCazoletasAct = _data.CubHorEncCazoletasAct,
                    CubHorEncCazoletasPUC = CalculatePUC(_data.CubHorEncCazoletas, "Horizontal"),
                    CubIncCompleta = _data.CubIncCompleta,
                    CubIncCompletaAct = _data.CubIncCompletaAct,
                    CubIncCompletaPUC = CalculatePUC(_data.CubIncCompleta, "Inclinada"),
                    CubIncFaldon = _data.CubIncFaldon,
                    CubIncFaldonAct = _data.CubIncFaldonAct,
                    CubIncFaldonPUC = CalculatePUC(_data.CubIncFaldon, "Inclinada"),
                    CubIncRemates = _data.CubIncRemates,
                    CubIncRematesAct = _data.CubIncRematesAct,
                    CubIncRematesPUC = CalculatePUC(_data.CubIncRemates, "Inclinada"),
                    CubIncEncParamVer = _data.CubIncEncParamVer,
                    CubIncEncParamVerAct = _data.CubIncEncParamVerAct,
                    CubIncEncParamVerPUC = CalculatePUC(_data.CubIncEncParamVer, "Inclinada"),
                    Climatizacion = _data.Climatizacion,
                    ClimatizacionAct = _data.ClimatizacionAct,
                    ClimatizacionPUC = CalculatePUC(_data.Climatizacion, "Aparatos Climatización"),
                    Radiadores = _data.Radiadores,
                    RadiadoresAct = _data.RadiadoresAct,
                    RadiadoresPUC = CalculatePUC(_data.Radiadores, "Radiadores"),
                    Circuitos = _data.Circuitos,
                    CircuitosAct = _data.CircuitosAct,
                    CircuitosPUC = CalculatePUC(_data.Circuitos, "Circuitos"),
                    LineasYDerivaciones = _data.LineasYDerivaciones,
                    LineasYDerivacionesAct = _data.LineasYDerivacionesAct,
                    LineasYDerivacionesPUC = CalculatePUC(_data.LineasYDerivaciones, "Líneas y Derivaciones"),
                    PuntosLuz = _data.PuntosLuz,
                    PuntosLuzAct = _data.PuntosLuzAct,
                    PuntosLuzPUC = CalculatePUC(_data.PuntosLuz, "Puntos de luz"),
                    TomaCorriente = _data.TomaCorriente,
                    TomaCorrienteAct = _data.TomaCorrienteAct,
                    TomaCorrientePUC = CalculatePUC(_data.TomaCorriente, "Toma de corriente"),
                    ConductorPuestaTierra = _data.ConductorPuestaTierra,
                    ConductorPuestaTierraAct = _data.ConductorPuestaTierraAct,
                    ConductorPuestaTierraPUC = CalculatePUC(_data.ConductorPuestaTierra, "Conductor de Puesta a Tierra"),
                    Canalizaciones = _data.Canalizaciones,
                    CanalizacionesAct = _data.CanalizacionesAct,
                    CanalizacionesPUC = CalculatePUC(_data.Canalizaciones, "Canalizaciones Agua Caliente"),
                    Desagues = _data.Desagues,
                    DesaguesAct = _data.DesaguesAct,
                    DesaguesPUC = CalculatePUC(_data.Desagues, "Desagües"),
                    CanalizacionesAguaFria = _data.CanalizacionesAguaFria,
                    CanalizacionesAguaFriaAct = _data.CanalizacionesAguaFriaAct,
                    CanalizacionesAguaFriaPUC = CalculatePUC(_data.CanalizacionesAguaFria, "Canalizaciones Agua Fría"),
                    Termos = _data.Termos,
                    TermosAct = _data.TermosAct,
                    TermosPUC = CalculatePUC(_data.Termos, "Termos/calentadores"),
                    Sanitarios = _data.Sanitarios,
                    SanitariosAct = _data.SanitariosAct,
                    SanitariosPUC = CalculatePUC(_data.Sanitarios, "Aparatos Sanitarios"),
                    CarpLigera = _data.CarpLigera,
                    CarpLigeraAct = _data.CarpLigeraAct,
                    CarpLigeraPUC = CalculatePUC(_data.CarpLigera, "Carpintería ligera"),
                    CarpMadera = _data.CarpMadera,
                    CarpMaderaAct = _data.CarpMaderaAct,
                    CarpMaderaPUC = CalculatePUC(_data.CarpMadera, "Carpintería madera. Ventanas"),
                    Rejas = _data.Rejas,
                    RejasAct = _data.RejasAct,
                    RejasPUC = CalculatePUC(_data.Rejas, "Rejas"),
                    Escalera = _data.Escalera,
                    EscaleraAct = _data.EscaleraAct,
                    EscaleraPUC = CalculatePUC(_data.Escalera, "Escalera"),
                    Rampa = _data.Rampa,
                    RampaAct = _data.RampaAct,
                    RampaPUC = CalculatePUC(_data.Rampa, "Rampa de minusválidos"),
                    Portero = _data.Portero,
                    PorteroAct = _data.PorteroAct,
                    PorteroPUC = CalculatePUC(_data.Portero, "Portero electrónico"),
                    Ascensores = _data.Ascensores,
                    AscensoresAct = _data.AscensoresAct,
                    AscensoresPUC = CalculatePUC(_data.Ascensores, "Ascensores")
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
                new HEParcial {Categoria = "Energía", Valor = SafeToDecimal(_result["Energia"]) * SafeToDecimal(_data.Superficie)},
                new HEParcial {Categoria = "Bosques", Valor = SafeToDecimal(_result["Bosques"]) * SafeToDecimal(_data.Superficie)},
                new HEParcial {Categoria = "Pastos", Valor = SafeToDecimal(_result["Pastos"])* SafeToDecimal(_data.Superficie)},
                new HEParcial {Categoria = "Mar", Valor = SafeToDecimal(_result["Mar"])* SafeToDecimal(_data.Superficie)},
                new HEParcial {Categoria = "Cultivos", Valor = SafeToDecimal(_result["Cultivos"])* SafeToDecimal(_data.Superficie)},
                new HEParcial {Categoria = "Superficie Consumida", Valor = SafeToDecimal(_result["SuperficieConsumida"])* SafeToDecimal(_data.Superficie)},
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

        private string CalculatePUC(object actuacion, string apartado)
        {
            switch (apartado)
            {
                case "Cimentaciones":
                    return BuscarCodigo(5, 5, actuacion.ToString());
                case "Arquetas":
                    return BuscarCodigo(7, 9, actuacion.ToString());
                case "Colectores":
                    return BuscarCodigo(11, 13, actuacion.ToString());
                case "Bajantes":
                    return BuscarCodigo(15, 16, actuacion.ToString());
                case "Forjados":
                    return BuscarCodigo(18, 18, actuacion.ToString());
                case "Particiones":
                    return BuscarCodigo(20, 23, actuacion.ToString());
                case "Cerramientos":
                    return BuscarCodigo(25, 34, actuacion.ToString());
                case "Fcas.interiores ladrillo":
                    return BuscarCodigo(36, 41, actuacion.ToString());
                case "Horizontal":
                    return BuscarCodigo(43, 50, actuacion.ToString());
                case "Inclinada":
                    return BuscarCodigo(52, 59, actuacion.ToString());
                case "Aparatos Climatización":
                    return BuscarCodigo(62, 62, actuacion.ToString());
                case "Radiadores":
                    return BuscarCodigo(64, 64, actuacion.ToString());
                case "Circuitos":
                    return BuscarCodigo(66, 66, actuacion.ToString());
                case "Líneas y Derivaciones":
                    return BuscarCodigo(68, 68, actuacion.ToString());
                case "Puntos de luz":
                    return BuscarCodigo(70, 70, actuacion.ToString());
                case "Toma de corriente":
                    return BuscarCodigo(72, 72, actuacion.ToString());
                case "Conductor de Puesta a Tierra":
                    return BuscarCodigo(74, 74, actuacion.ToString());
                case "Canalizaciones Agua Caliente":
                    return BuscarCodigo(76, 77, actuacion.ToString());
                case "Desagües":
                    return BuscarCodigo(79, 79, actuacion.ToString());
                case "Canalizaciones Agua Fría":
                    return BuscarCodigo(81, 82, actuacion.ToString());
                case "Aparatos Sanitarios":
                    return BuscarCodigo(84, 84, actuacion.ToString());
                case "Termos/calentadores":
                    return BuscarCodigo(86, 87, actuacion.ToString());
                case "Carpintería ligera":
                    return BuscarCodigo(89, 91, actuacion.ToString());
                case "Carpintería madera. Ventanas":
                    return BuscarCodigo(93, 95, actuacion.ToString());
                case "Rejas":
                    return BuscarCodigo(97, 98, actuacion.ToString());
                case "Ascensores":
                    return BuscarCodigo(100, 100, actuacion.ToString());
                case "Escalera":
                    return BuscarCodigo(102, 103, actuacion.ToString());
                case "Rampa de minusválidos":
                    return BuscarCodigo(105, 105, actuacion.ToString());
                case "Portero electrónico":
                    return BuscarCodigo(107, 107, actuacion.ToString());
            }
            return string.Empty;
        }

        private string BuscarCodigo(int y1, int y2, string actuacion)
        {
            for (int j = y1; j <= y2; j++)
            {
                if (_sheetDespl.Cells[j, 4].Value == actuacion)
                {
                    return _sheetDespl.Cells[j, 3].Value;
                }
            }
            return string.Empty;
        }
    }
}