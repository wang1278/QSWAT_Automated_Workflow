import init_file as variables
import cj_function_lib as cj
from datetime import datetime

wgn_table = cj.extract_table_from_mdb(
    variables.ProjMDB, "wgn", variables.path + "\\wgn.tmp~")
now = datetime.now()

DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
    str(now.year) + " " + str(now.time()).split(".")[0]
SWAT_Vers = "QSWAT Workflow v1.5"

for hru_record in wgn_table:

    # Hru ID
    WshedHRU = hru_record.split(",")[0].strip('"')
    SubBasin = hru_record.split(",")[1].strip('"')

    # Parameters
    STATION	=	hru_record.split(",")[2].strip('"')
    WLATITUDE	=	hru_record.split(",")[3].strip('"')
    WLONGITUDE	=	hru_record.split(",")[4].strip('"')
    WELEV	=	hru_record.split(",")[5].strip('"')
    RAIN_YRS	=	hru_record.split(",")[6].strip('"')
    TMPMX1	=	hru_record.split(",")[7].strip('"')
    TMPMX2	=	hru_record.split(",")[8].strip('"')
    TMPMX3	=	hru_record.split(",")[9].strip('"')
    TMPMX4	=	hru_record.split(",")[10].strip('"')
    TMPMX5	=	hru_record.split(",")[11].strip('"')
    TMPMX6	=	hru_record.split(",")[12].strip('"')
    TMPMX7	=	hru_record.split(",")[13].strip('"')
    TMPMX8	=	hru_record.split(",")[14].strip('"')
    TMPMX9	=	hru_record.split(",")[15].strip('"')
    TMPMX10	=	hru_record.split(",")[16].strip('"')
    TMPMX11	=	hru_record.split(",")[17].strip('"')
    TMPMX12	=	hru_record.split(",")[18].strip('"')
    TMPMN1	=	hru_record.split(",")[19].strip('"')
    TMPMN2	=	hru_record.split(",")[20].strip('"')
    TMPMN3	=	hru_record.split(",")[21].strip('"')
    TMPMN4	=	hru_record.split(",")[22].strip('"')
    TMPMN5	=	hru_record.split(",")[23].strip('"')
    TMPMN6	=	hru_record.split(",")[24].strip('"')
    TMPMN7	=	hru_record.split(",")[25].strip('"')
    TMPMN8	=	hru_record.split(",")[26].strip('"')
    TMPMN9	=	hru_record.split(",")[27].strip('"')
    TMPMN10	=	hru_record.split(",")[28].strip('"')
    TMPMN11	=	hru_record.split(",")[29].strip('"')
    TMPMN12	=	hru_record.split(",")[30].strip('"')
    TMPSTDMX1	=	hru_record.split(",")[31].strip('"')
    TMPSTDMX2	=	hru_record.split(",")[32].strip('"')
    TMPSTDMX3	=	hru_record.split(",")[33].strip('"')
    TMPSTDMX4	=	hru_record.split(",")[34].strip('"')
    TMPSTDMX5	=	hru_record.split(",")[35].strip('"')
    TMPSTDMX6	=	hru_record.split(",")[36].strip('"')
    TMPSTDMX7	=	hru_record.split(",")[37].strip('"')
    TMPSTDMX8	=	hru_record.split(",")[38].strip('"')
    TMPSTDMX9	=	hru_record.split(",")[39].strip('"')
    TMPSTDMX10	=	hru_record.split(",")[40].strip('"')
    TMPSTDMX11	=	hru_record.split(",")[41].strip('"')
    TMPSTDMX12	=	hru_record.split(",")[42].strip('"')
    TMPSTDMN1	=	hru_record.split(",")[43].strip('"')
    TMPSTDMN2	=	hru_record.split(",")[44].strip('"')
    TMPSTDMN3	=	hru_record.split(",")[45].strip('"')
    TMPSTDMN4	=	hru_record.split(",")[46].strip('"')
    TMPSTDMN5	=	hru_record.split(",")[47].strip('"')
    TMPSTDMN6	=	hru_record.split(",")[48].strip('"')
    TMPSTDMN7	=	hru_record.split(",")[49].strip('"')
    TMPSTDMN8	=	hru_record.split(",")[50].strip('"')
    TMPSTDMN9	=	hru_record.split(",")[51].strip('"')
    TMPSTDMN10	=	hru_record.split(",")[52].strip('"')
    TMPSTDMN11	=	hru_record.split(",")[53].strip('"')
    TMPSTDMN12	=	hru_record.split(",")[54].strip('"')
    PCPMM1	=	hru_record.split(",")[55].strip('"')
    PCPMM2	=	hru_record.split(",")[56].strip('"')
    PCPMM3	=	hru_record.split(",")[57].strip('"')
    PCPMM4	=	hru_record.split(",")[58].strip('"')
    PCPMM5	=	hru_record.split(",")[59].strip('"')
    PCPMM6	=	hru_record.split(",")[60].strip('"')
    PCPMM7	=	hru_record.split(",")[61].strip('"')
    PCPMM8	=	hru_record.split(",")[62].strip('"')
    PCPMM9	=	hru_record.split(",")[63].strip('"')
    PCPMM10	=	hru_record.split(",")[64].strip('"')
    PCPMM11	=	hru_record.split(",")[65].strip('"')
    PCPMM12	=	hru_record.split(",")[66].strip('"')
    PCPSTD1	=	hru_record.split(",")[67].strip('"')
    PCPSTD2	=	hru_record.split(",")[68].strip('"')
    PCPSTD3	=	hru_record.split(",")[69].strip('"')
    PCPSTD4	=	hru_record.split(",")[70].strip('"')
    PCPSTD5	=	hru_record.split(",")[71].strip('"')
    PCPSTD6	=	hru_record.split(",")[72].strip('"')
    PCPSTD7	=	hru_record.split(",")[73].strip('"')
    PCPSTD8	=	hru_record.split(",")[74].strip('"')
    PCPSTD9	=	hru_record.split(",")[75].strip('"')
    PCPSTD10	=	hru_record.split(",")[76].strip('"')
    PCPSTD11	=	hru_record.split(",")[77].strip('"')
    PCPSTD12	=	hru_record.split(",")[78].strip('"')
    PCPSKW1	=	hru_record.split(",")[79].strip('"')
    PCPSKW2	=	hru_record.split(",")[80].strip('"')
    PCPSKW3	=	hru_record.split(",")[81].strip('"')
    PCPSKW4	=	hru_record.split(",")[82].strip('"')
    PCPSKW5	=	hru_record.split(",")[83].strip('"')
    PCPSKW6	=	hru_record.split(",")[84].strip('"')
    PCPSKW7	=	hru_record.split(",")[85].strip('"')
    PCPSKW8	=	hru_record.split(",")[86].strip('"')
    PCPSKW9	=	hru_record.split(",")[87].strip('"')
    PCPSKW10	=	hru_record.split(",")[88].strip('"')
    PCPSKW11	=	hru_record.split(",")[89].strip('"')
    PCPSKW12	=	hru_record.split(",")[90].strip('"')
    PR_W11	=	hru_record.split(",")[91].strip('"')
    PR_W12	=	hru_record.split(",")[92].strip('"')
    PR_W13	=	hru_record.split(",")[93].strip('"')
    PR_W14	=	hru_record.split(",")[94].strip('"')
    PR_W15	=	hru_record.split(",")[95].strip('"')
    PR_W16	=	hru_record.split(",")[96].strip('"')
    PR_W17	=	hru_record.split(",")[97].strip('"')
    PR_W18	=	hru_record.split(",")[98].strip('"')
    PR_W19	=	hru_record.split(",")[99].strip('"')
    PR_W110	=	hru_record.split(",")[100].strip('"')
    PR_W111	=	hru_record.split(",")[101].strip('"')
    PR_W112	=	hru_record.split(",")[102].strip('"')
    PR_W21	=	hru_record.split(",")[103].strip('"')
    PR_W22	=	hru_record.split(",")[104].strip('"')
    PR_W23	=	hru_record.split(",")[105].strip('"')
    PR_W24	=	hru_record.split(",")[106].strip('"')
    PR_W25	=	hru_record.split(",")[107].strip('"')
    PR_W26	=	hru_record.split(",")[108].strip('"')
    PR_W27	=	hru_record.split(",")[109].strip('"')
    PR_W28	=	hru_record.split(",")[110].strip('"')
    PR_W29	=	hru_record.split(",")[111].strip('"')
    PR_W210	=	hru_record.split(",")[112].strip('"')
    PR_W211	=	hru_record.split(",")[113].strip('"')
    PR_W212	=	hru_record.split(",")[114].strip('"')
    PCPD1	=	hru_record.split(",")[115].strip('"')
    PCPD2	=	hru_record.split(",")[116].strip('"')
    PCPD3	=	hru_record.split(",")[117].strip('"')
    PCPD4	=	hru_record.split(",")[118].strip('"')
    PCPD5	=	hru_record.split(",")[119].strip('"')
    PCPD6	=	hru_record.split(",")[120].strip('"')
    PCPD7	=	hru_record.split(",")[121].strip('"')
    PCPD8	=	hru_record.split(",")[122].strip('"')
    PCPD9	=	hru_record.split(",")[123].strip('"')
    PCPD10	=	hru_record.split(",")[124].strip('"')
    PCPD11	=	hru_record.split(",")[125].strip('"')
    PCPD12	=	hru_record.split(",")[126].strip('"')
    RAINHHMX1	=	hru_record.split(",")[127].strip('"')
    RAINHHMX2	=	hru_record.split(",")[128].strip('"')
    RAINHHMX3	=	hru_record.split(",")[129].strip('"')
    RAINHHMX4	=	hru_record.split(",")[130].strip('"')
    RAINHHMX5	=	hru_record.split(",")[131].strip('"')
    RAINHHMX6	=	hru_record.split(",")[132].strip('"')
    RAINHHMX7	=	hru_record.split(",")[133].strip('"')
    RAINHHMX8	=	hru_record.split(",")[134].strip('"')
    RAINHHMX9	=	hru_record.split(",")[135].strip('"')
    RAINHHMX10	=	hru_record.split(",")[136].strip('"')
    RAINHHMX11	=	hru_record.split(",")[137].strip('"')
    RAINHHMX12	=	hru_record.split(",")[138].strip('"')
    SOLARAV1	=	hru_record.split(",")[139].strip('"')
    SOLARAV2	=	hru_record.split(",")[140].strip('"')
    SOLARAV3	=	hru_record.split(",")[141].strip('"')
    SOLARAV4	=	hru_record.split(",")[142].strip('"')
    SOLARAV5	=	hru_record.split(",")[143].strip('"')
    SOLARAV6	=	hru_record.split(",")[144].strip('"')
    SOLARAV7	=	hru_record.split(",")[145].strip('"')
    SOLARAV8	=	hru_record.split(",")[146].strip('"')
    SOLARAV9	=	hru_record.split(",")[147].strip('"')
    SOLARAV10	=	hru_record.split(",")[148].strip('"')
    SOLARAV11	=	hru_record.split(",")[149].strip('"')
    SOLARAV12	=	hru_record.split(",")[150].strip('"')
    DEWPT1	=	hru_record.split(",")[151].strip('"')
    DEWPT2	=	hru_record.split(",")[152].strip('"')
    DEWPT3	=	hru_record.split(",")[153].strip('"')
    DEWPT4	=	hru_record.split(",")[154].strip('"')
    DEWPT5	=	hru_record.split(",")[155].strip('"')
    DEWPT6	=	hru_record.split(",")[156].strip('"')
    DEWPT7	=	hru_record.split(",")[157].strip('"')
    DEWPT8	=	hru_record.split(",")[158].strip('"')
    DEWPT9	=	hru_record.split(",")[159].strip('"')
    DEWPT10	=	hru_record.split(",")[160].strip('"')
    DEWPT11	=	hru_record.split(",")[161].strip('"')
    DEWPT12	=	hru_record.split(",")[162].strip('"')
    WNDAV1	=	hru_record.split(",")[163].strip('"')
    WNDAV2	=	hru_record.split(",")[164].strip('"')
    WNDAV3	=	hru_record.split(",")[165].strip('"')
    WNDAV4	=	hru_record.split(",")[166].strip('"')
    WNDAV5	=	hru_record.split(",")[167].strip('"')
    WNDAV6	=	hru_record.split(",")[168].strip('"')
    WNDAV7	=	hru_record.split(",")[169].strip('"')
    WNDAV8	=	hru_record.split(",")[170].strip('"')
    WNDAV9	=	hru_record.split(",")[171].strip('"')
    WNDAV10	=	hru_record.split(",")[172].strip('"')
    WNDAV11	=	hru_record.split(",")[173].strip('"')
    WNDAV12	=	hru_record.split(",")[174].strip('"')

    # Building String
    wgn_file = " .Wgn file Subbasin: " + SubBasin + " STATION NAME:" + STATION + " " + DateAndTime + " " + SWAT_Vers + \
        "\n  LATITUDE =" + cj.trailing_spaces(int(7),WLATITUDE,2) + " LONGITUDE =" + cj.trailing_spaces(int(7),WLONGITUDE,2) + \
        "\n  ELEV [m] =" + cj.trailing_spaces(int(7),WELEV,2) + \
        "\n  RAIN_YRS =" + cj.trailing_spaces(int(7),RAIN_YRS,2) + \
        "\n" + cj.trailing_spaces(int(6),TMPMX1,2) + cj.trailing_spaces(int(6),TMPMX2,2) + cj.trailing_spaces(int(6),TMPMX3,2) + cj.trailing_spaces(int(6),TMPMX4,2) + cj.trailing_spaces(int(6),TMPMX5,2) + cj.trailing_spaces(int(6),TMPMX6,2) + cj.trailing_spaces(int(6),TMPMX7,2) + cj.trailing_spaces(int(6),TMPMX8,2) + cj.trailing_spaces(int(6),TMPMX9,2) + cj.trailing_spaces(int(6),TMPMX10,2) + cj.trailing_spaces(int(6),TMPMX11,2) + cj.trailing_spaces(int(6),TMPMX12,2) + \
        "\n" + cj.trailing_spaces(int(6),TMPMN1,2) + cj.trailing_spaces(int(6),TMPMN2,2) + cj.trailing_spaces(int(6),TMPMN3,2) + cj.trailing_spaces(int(6),TMPMN4,2) + cj.trailing_spaces(int(6),TMPMN5,2) + cj.trailing_spaces(int(6),TMPMN6,2) + cj.trailing_spaces(int(6),TMPMN7,2) + cj.trailing_spaces(int(6),TMPMN8,2) + cj.trailing_spaces(int(6),TMPMN9,2) + cj.trailing_spaces(int(6),TMPMN10,2) + cj.trailing_spaces(int(6),TMPMN11,2) + cj.trailing_spaces(int(6),TMPMN12,2) + \
        "\n" + cj.trailing_spaces(int(6),TMPSTDMX1,2) + cj.trailing_spaces(int(6),TMPSTDMX2,2) + cj.trailing_spaces(int(6),TMPSTDMX3,2) + cj.trailing_spaces(int(6),TMPSTDMX4,2) + cj.trailing_spaces(int(6),TMPSTDMX5,2) + cj.trailing_spaces(int(6),TMPSTDMX6,2) + cj.trailing_spaces(int(6),TMPSTDMX7,2) + cj.trailing_spaces(int(6),TMPSTDMX8,2) + cj.trailing_spaces(int(6),TMPSTDMX9,2) + cj.trailing_spaces(int(6),TMPSTDMX10,2) + cj.trailing_spaces(int(6),TMPSTDMX11,2) + cj.trailing_spaces(int(6),TMPSTDMX12,2) + \
        "\n" + cj.trailing_spaces(int(6),TMPSTDMN1,2) + cj.trailing_spaces(int(6),TMPSTDMN2,2) + cj.trailing_spaces(int(6),TMPSTDMN3,2) + cj.trailing_spaces(int(6),TMPSTDMN4,2) + cj.trailing_spaces(int(6),TMPSTDMN5,2) + cj.trailing_spaces(int(6),TMPSTDMN6,2) + cj.trailing_spaces(int(6),TMPSTDMN7,2) + cj.trailing_spaces(int(6),TMPSTDMN8,2) + cj.trailing_spaces(int(6),TMPSTDMN9,2) + cj.trailing_spaces(int(6),TMPSTDMN10,2) + cj.trailing_spaces(int(6),TMPSTDMN11,2) + cj.trailing_spaces(int(6),TMPSTDMN12,2) + \
        "\n" + cj.trailing_spaces(int(6),PCPMM1,1) + cj.trailing_spaces(int(6),PCPMM2,1) + cj.trailing_spaces(int(6),PCPMM3,1) + cj.trailing_spaces(int(6),PCPMM4,1) + cj.trailing_spaces(int(6),PCPMM5,1) + cj.trailing_spaces(int(6),PCPMM6,1) + cj.trailing_spaces(int(6),PCPMM7,1) + cj.trailing_spaces(int(6),PCPMM8,1) + cj.trailing_spaces(int(6),PCPMM9,1) + cj.trailing_spaces(int(6),PCPMM10,1) + cj.trailing_spaces(int(6),PCPMM11,1) + cj.trailing_spaces(int(6),PCPMM12,1) + \
        "\n" + cj.trailing_spaces(int(6),PCPSTD1,2) + cj.trailing_spaces(int(6),PCPSTD2,2) + cj.trailing_spaces(int(6),PCPSTD3,2) + cj.trailing_spaces(int(6),PCPSTD4,2) + cj.trailing_spaces(int(6),PCPSTD5,2) + cj.trailing_spaces(int(6),PCPSTD6,2) + cj.trailing_spaces(int(6),PCPSTD7,2) + cj.trailing_spaces(int(6),PCPSTD8,2) + cj.trailing_spaces(int(6),PCPSTD9,2) + cj.trailing_spaces(int(6),PCPSTD10,2) + cj.trailing_spaces(int(6),PCPSTD11,2) + cj.trailing_spaces(int(6),PCPSTD12,2) + \
        "\n" + cj.trailing_spaces(int(6),PCPSKW1,2) + cj.trailing_spaces(int(6),PCPSKW2,2) + cj.trailing_spaces(int(6),PCPSKW3,2) + cj.trailing_spaces(int(6),PCPSKW4,2) + cj.trailing_spaces(int(6),PCPSKW5,2) + cj.trailing_spaces(int(6),PCPSKW6,2) + cj.trailing_spaces(int(6),PCPSKW7,2) + cj.trailing_spaces(int(6),PCPSKW8,2) + cj.trailing_spaces(int(6),PCPSKW9,2) + cj.trailing_spaces(int(6),PCPSKW10,2) + cj.trailing_spaces(int(6),PCPSKW11,2) + cj.trailing_spaces(int(6),PCPSKW12,2) + \
        "\n" + cj.trailing_spaces(int(6),PR_W11,2) + cj.trailing_spaces(int(6),PR_W12,2) + cj.trailing_spaces(int(6),PR_W13,2) + cj.trailing_spaces(int(6),PR_W14,2) + cj.trailing_spaces(int(6),PR_W15,2) + cj.trailing_spaces(int(6),PR_W16,2) + cj.trailing_spaces(int(6),PR_W17,2) + cj.trailing_spaces(int(6),PR_W18,2) + cj.trailing_spaces(int(6),PR_W19,2) + cj.trailing_spaces(int(6),PR_W110,2) + cj.trailing_spaces(int(6),PR_W111,2) + cj.trailing_spaces(int(6),PR_W112,2) + \
        "\n" + cj.trailing_spaces(int(6),PR_W21,2) + cj.trailing_spaces(int(6),PR_W22,2) + cj.trailing_spaces(int(6),PR_W23,2) + cj.trailing_spaces(int(6),PR_W24,2) + cj.trailing_spaces(int(6),PR_W25,2) + cj.trailing_spaces(int(6),PR_W26,2) + cj.trailing_spaces(int(6),PR_W27,2) + cj.trailing_spaces(int(6),PR_W28,2) + cj.trailing_spaces(int(6),PR_W29,2) + cj.trailing_spaces(int(6),PR_W210,2) + cj.trailing_spaces(int(6),PR_W211,2) + cj.trailing_spaces(int(6),PR_W212,2) + \
        "\n" + cj.trailing_spaces(int(6),PCPD1,2) + cj.trailing_spaces(int(6),PCPD2,2) + cj.trailing_spaces(int(6),PCPD3,2) + cj.trailing_spaces(int(6),PCPD4,2) + cj.trailing_spaces(int(6),PCPD5,2) + cj.trailing_spaces(int(6),PCPD6,2) + cj.trailing_spaces(int(6),PCPD7,2) + cj.trailing_spaces(int(6),PCPD8,2) + cj.trailing_spaces(int(6),PCPD9,2) + cj.trailing_spaces(int(6),PCPD10,2) + cj.trailing_spaces(int(6),PCPD11,2) + cj.trailing_spaces(int(6),PCPD12,2) + \
        "\n" + cj.trailing_spaces(int(6),RAINHHMX1,2) + cj.trailing_spaces(int(6),RAINHHMX2,2) + cj.trailing_spaces(int(6),RAINHHMX3,2) + cj.trailing_spaces(int(6),RAINHHMX4,2) + cj.trailing_spaces(int(6),RAINHHMX5,2) + cj.trailing_spaces(int(6),RAINHHMX6,2) + cj.trailing_spaces(int(6),RAINHHMX7,2) + cj.trailing_spaces(int(6),RAINHHMX8,2) + cj.trailing_spaces(int(6),RAINHHMX9,2) + cj.trailing_spaces(int(6),RAINHHMX10,2) + cj.trailing_spaces(int(6),RAINHHMX11,2) + cj.trailing_spaces(int(6),RAINHHMX12,2) + \
        "\n" + cj.trailing_spaces(int(6),SOLARAV1,2) + cj.trailing_spaces(int(6),SOLARAV2,2) + cj.trailing_spaces(int(6),SOLARAV3,2) + cj.trailing_spaces(int(6),SOLARAV4,2) + cj.trailing_spaces(int(6),SOLARAV5,2) + cj.trailing_spaces(int(6),SOLARAV6,2) + cj.trailing_spaces(int(6),SOLARAV7,2) + cj.trailing_spaces(int(6),SOLARAV8,2) + cj.trailing_spaces(int(6),SOLARAV9,2) + cj.trailing_spaces(int(6),SOLARAV10,2) + cj.trailing_spaces(int(6),SOLARAV11,2) + cj.trailing_spaces(int(6),SOLARAV12,2) + \
        "\n" + cj.trailing_spaces(int(6),DEWPT1,2) + cj.trailing_spaces(int(6),DEWPT2,2) + cj.trailing_spaces(int(6),DEWPT3,2) + cj.trailing_spaces(int(6),DEWPT4,2) + cj.trailing_spaces(int(6),DEWPT5,2) + cj.trailing_spaces(int(6),DEWPT6,2) + cj.trailing_spaces(int(6),DEWPT7,2) + cj.trailing_spaces(int(6),DEWPT8,2) + cj.trailing_spaces(int(6),DEWPT9,2) + cj.trailing_spaces(int(6),DEWPT10,2) + cj.trailing_spaces(int(6),DEWPT11,2) + cj.trailing_spaces(int(6),DEWPT12,2) + \
        "\n" + cj.trailing_spaces(int(6),WNDAV1,2) + cj.trailing_spaces(int(6),WNDAV2,2) + cj.trailing_spaces(int(6),WNDAV3,2) + cj.trailing_spaces(int(6),WNDAV4,2) + cj.trailing_spaces(int(6),WNDAV5,2) + cj.trailing_spaces(int(6),WNDAV6,2) + cj.trailing_spaces(int(6),WNDAV7,2) + cj.trailing_spaces(int(6),WNDAV8,2) + cj.trailing_spaces(int(6),WNDAV9,2) + cj.trailing_spaces(int(6),WNDAV10,2) + cj.trailing_spaces(int(6),WNDAV11,2) + cj.trailing_spaces(int(6),WNDAV12,2) + \
        "\n"

    fileName = cj.get_filename(int(SubBasin), int(0), "wgn")
    cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, wgn_file)
    #print fileName

