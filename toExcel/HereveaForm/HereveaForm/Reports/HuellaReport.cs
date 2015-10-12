using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Text;

namespace Herevea.Reports
{
    public class HuellaReportDTO
    {
        public string Provincia { get; set; }
        public string Municipio { get; set; }
        public string Direccion { get; set; }
        public string RefCatastral { get; set; }

        public decimal Superficie { get; set; }
        public int NumeroPlantas { get; set; }
        public decimal AlturaEdificio { get; set; }

        public decimal HuellaTotalSuperficie { get; set; }
        public decimal HuellaTotal { get; set; }

        public decimal HuellaDemolicionSuperficie { get; set; }
        public decimal HuellaDemolicion { get; set; }

        public decimal HuellaConstruccionSuperficie { get; set; }
        public decimal HuellaConstruccion { get; set; }

        public decimal HEEn { get; set; }
        public decimal HEBo { get; set; }
        public decimal HEPa { get; set; }
        public decimal HEMa { get; set; }
        public decimal HECu { get; set; }
        public decimal HESu { get; set; }

        public decimal HEEnSuperficie { get; set; }
        public decimal HEBoSuperficie { get; set; }
        public decimal HEPaSuperficie { get; set; }
        public decimal HEMaSuperficie { get; set; }
        public decimal HECuSuperficie { get; set; }
        public decimal HESuSuperficie { get; set; }

        public decimal? MaqEn { get; set; }
        public decimal? MaqBo { get; set; }
        public decimal? MaqPa { get; set; }
        public decimal? MaqMa { get; set; }
        public decimal? MaqCu { get; set; }
        public decimal? MaqSu { get; set; }

        public decimal? EleEn { get; set; }
        public decimal? EleBo { get; set; }
        public decimal? ElePa { get; set; }
        public decimal? EleMa { get; set; }
        public decimal? EleCu { get; set; }
        public decimal? EleSu { get; set; }

        public decimal? AgEn { get; set; }
        public decimal? AgBo { get; set; }
        public decimal? AgPa { get; set; }
        public decimal? AgMa { get; set; }
        public decimal? AgCu { get; set; }
        public decimal? AgSu { get; set; }

        public decimal? AliEn { get; set; }
        public decimal? AliBo { get; set; }
        public decimal? AliPa { get; set; }
        public decimal? AliMa { get; set; }
        public decimal? AliCu { get; set; }
        public decimal? AliSu { get; set; }

        public decimal? MovEn { get; set; }
        public decimal? MovBo { get; set; }
        public decimal? MovPa { get; set; }
        public decimal? MovMa { get; set; }
        public decimal? MovCu { get; set; }
        public decimal? MovSu { get; set; }

        public decimal? RsuEn { get; set; }
        public decimal? RsuBo { get; set; }
        public decimal? RsuPa { get; set; }
        public decimal? RsuMa { get; set; }
        public decimal? RsuCu { get; set; }
        public decimal? RsuSu { get; set; }
        
        public decimal? MatEn { get; set; }
        public decimal? MatBo { get; set; }
        public decimal? MatPa { get; set; }
        public decimal? MatMa { get; set; }
        public decimal? MatCu { get; set; }
        public decimal? MatSu { get; set; }

        public decimal? RcdEn { get; set; }
        public decimal? RcdBo { get; set; }
        public decimal? RcdPa { get; set; }
        public decimal? RcdMa { get; set; }
        public decimal? RcdCu { get; set; }
        public decimal? RcdSu { get; set; }

        public decimal? OcuEn { get; set; }
        public decimal? OcuBo { get; set; }
        public decimal? OcuPa { get; set; }
        public decimal? OcuMa { get; set; }
        public decimal? OcuCu { get; set; }
        public decimal? OcuSu { get; set; }
    }

    public class Energias
    {
        public decimal Impacto { get; set; }
        public string Categoria { get; set; }
    }

    public class HEParcial
    {
        public decimal Valor { get; set; }
        public string Categoria { get; set; }
    }

    public class Actuaciones
    {
        public string Pilotes { get; set; }
        public string PilotesAct { get; set; }
        public string Arquetas { get; set; }
        public string ArquetasAct { get; set; }
        public string Colectores { get; set; }
        public string ColectoresAct { get; set; }
        public string Bajantes { get; set; }
        public string BajantesAct { get; set; }
        public string Forjados { get; set; }
        public string ForjadosAct { get; set; }
        public string Fisuras { get; set; }
        public string FisurasAct { get; set; }
        public string Grietas { get; set; }
        public string GrietasAct { get; set; }
        public string LadFisuras { get; set; }
        public string LadFisurasAct { get; set; }
        public string LadGrietas { get; set; }
        public string LadGrietasAct { get; set; }
        public string LadHumSuelo { get; set; }
        public string LadHumSueloAct { get; set; }
        public string LadHumTecho { get; set; }
        public string LadHumTechoAct { get; set; }
        public string IntFisuras { get; set; }
        public string IntFisurasAct { get; set; }
        public string IntGrietas { get; set; }
        public string IntGrietasAct { get; set; }
        public string HumSuelo { get; set; }
        public string HumSueloAct { get; set; }
        public string CubHorCom { get; set; }
        public string CubHorComAct { get; set; }
        public string CubHorFaldon { get; set; }
        public string CubHorFaldonAct { get; set; }
        public string CubHorEncParamVer { get; set; }
        public string CubHorEncParamVerAct { get; set; }
        public string CubHorEncCazoletas { get; set; }
        public string CubHorEncCazoletasAct { get; set; }
        public string CubIncCompleta { get; set; }
        public string CubIncCompletaAct { get; set; }
        public string CubIncFaldon { get; set; }
        public string CubIncFaldonAct { get; set; }
        public string CubIncRemates { get; set; }
        public string CubIncRematesAct { get; set; }
        public string CubIncEncParamVer { get; set; }
        public string CubIncEncParamVerAct { get; set; }
        public string Climatizacion { get; set; }
        public string ClimatizacionAct { get; set; }
        public string Radiadores { get; set; }
        public string RadiadoresAct { get; set; }
        public string Circuitos { get; set; }
        public string CircuitosAct { get; set; }
        public string LineasYDerivaciones { get; set; }
        public string LineasYDerivacionesAct { get; set; }
        public string PuntosLuz { get; set; }
        public string PuntosLuzAct { get; set; }
        public string TomaCorriente { get; set; }
        public string TomaCorrienteAct { get; set; }
        public string ConductorPuestaTierra { get; set; }
        public string ConductorPuestaTierraAct { get; set; }
        public string Canalizaciones { get; set; }
        public string CanalizacionesAct { get; set; }
        public string Desagues { get; set; }
        public string DesaguesAct { get; set; }
        public string CanalizacionesAguaFria { get; set; }
        public string CanalizacionesAguaFriaAct { get; set; }
        public string Termos { get; set; }
        public string TermosAct { get; set; }
        public string Sanitarios { get; set; }
        public string SanitariosAct { get; set; }
        public string CarpLigera { get; set; }
        public string CarpLigeraAct { get; set; }
        public string CarpMadera { get; set; }
        public string CarpMaderaAct { get; set; }
        public string Rejas { get; set; }
        public string RejasAct { get; set; }
        public string Escalera { get; set; }
        public string EscaleraAct { get; set; }
        public string Rampa { get; set; }
        public string RampaAct { get; set; }
        public string Portero { get; set; }
        public string PorteroAct { get; set; }
        public string Ascensores { get; set; }
        public string AscensoresAct { get; set; }
        public string PilotesPUC { get; set; }
        public string ArquetasPUC { get; set; }
        public string ColectoresPUC { get; set; }
        public string BajantesPUC { get; set; }
        public string ForjadosPUC { get; set; }
        public string FisurasPUC { get; set; }
        public string GrietasPUC { get; set; }
        public string LadFisurasPUC { get; set; }
        public string LadGrietasPUC { get; set; }
        public string LadHumSueloPUC { get; set; }
        public string LadHumTechoPUC { get; set; }
        public string IntFisurasPUC { get; set; }
        public string IntGrietasPUC { get; set; }
        public string HumSueloPUC { get; set; }
        public string CubHorComPUC { get; set; }
        public string CubHorFaldonPUC { get; set; }
        public string CubHorEncParamVerPUC { get; set; }
        public string CubHorEncCazoletasPUC { get; set; }
        public string CubIncCompletaPUC { get; set; }
        public string CubIncFaldonPUC { get; set; }
        public string CubIncRematesPUC { get; set; }
        public string CubIncEncParamVerPUC { get; set; }
        public string ClimatizacionPUC { get; set; }
        public string RadiadoresPUC { get; set; }
        public string CircuitosPUC { get; set; }
        public string LineasYDerivacionesPUC { get; set; }
        public string PuntosLuzPUC { get; set; }
        public string TomaCorrientePUC { get; set; }
        public string ConductorPuestaTierraPUC { get; set; }
        public string CanalizacionesPUC { get; set; }
        public string DesaguesPUC { get; set; }
        public string CanalizacionesAguaFriaPUC { get; set; }
        public string TermosPUC { get; set; }
        public string SanitariosPUC { get; set; }
        public string CarpLigeraPUC { get; set; }
        public string CarpMaderaPUC { get; set; }
        public string RejasPUC { get; set; }
        public string EscaleraPUC { get; set; }
        public string RampaPUC { get; set; }
        public string PorteroPUC { get; set; }
        public string AscensoresPUC { get; set; }
    }

    public class PEM
    {
        public decimal Cimentaciones { get; set; }
        public decimal Saneamiento { get; set; }
        public decimal Estructuras { get; set; }
        public decimal Albañileria { get; set; }
        public decimal Cubiertas { get; set; }
        public decimal Instalaciones { get; set; }
        public decimal Carpinteria { get; set; }
        public decimal Accesibilidad { get; set; }
        public decimal Residuos { get; set; }

        public decimal Rehabilitacion { get; set; }

        public decimal DemolicionEdificio { get; set; }
        public decimal DemolicionResiduos { get; set; }

        public decimal Construccion { get; set; }
    }
}
