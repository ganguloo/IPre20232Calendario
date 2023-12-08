import os

PATH_LISTADO_NRC = os.path.join("excel_horarios",
                                 "Prueba_nrc.xlsx")
PATH_LISTADO_NRC_ORIGINAL = os.path.join("excel_horarios",
                                 "Listado_NRC_2023_Enero.xlsx")
PATH_VACANTES = os.path.join("instancia_datos", "vacantes.xlsx")
PATH_CONEXIONES = os.path.join("instancia_datos", "conexiones.xlsx")
PATH_CURSOS_IES = os.path.join(
        "excel_horarios", "Prueba_ies.xlsx")
PATH_CURSOS_IES_ORIGINAL = os.path.join(
        "excel_horarios", "004 - Listado_NRC_Programados.xlsx")
# PATH_CURSOS_IES = os.path.join(
#     "excel_horarios", "004-filtrado.xlsx")


PATH_MATERIAS = os.path.join("excel_horarios", "Listado_materias.xlsx")
PATH_LISTADO_CURSOS = os.path.join("instancia_datos", "listado_cursos.xlsx")

NUM_EXPERIMENTO = 2



FECHAS_PROHIBIDAS_MARZO_GENERAL = ["06-Mar", "07-Mar", "08-Mar", "09-Mar", "10-Mar",
                                   "11-Mar", "12-Mar", "13-Mar", "14-Mar", "15-Mar",
                                   "16-Mar", "17-Mar", "18-Mar", "19-Mar", "20-Mar",
                                   "21-Mar", "22-Mar", "23-Mar", "24-Mar", "25-Mar",
                                   "26-Mar", "27-Mar", "28-Mar", "29-Mar", "30-Mar",
                                   ]

FECHAS_PROHIBIDAS_ABRIL_GENERAL = ["02-Apr", "04-Apr", "05-Apr", "06-Apr", "09-Apr",
                                   "10-Apr", "11-Apr", "12-Apr", "16-Apr", "23-Apr",
                                   "30-Apr"]

FECHAS_PROHIBIDAS_MAYO_GENERAL = ["01-May", "02-May", "03-May", "04-May", "07-May",
                                  "08-May", "09-May", "14-May", "21-May", "28-May",
                                  "31-May"]

FECHAS_PROHIBIDAS_JUNIO_GENERAL = ["04-Jun", "07-Jun", "11-Jun", "18-Jun", "21-Jun",
                                   "25-Jun", "26-Jun"]

FECHAS_PROHIBIDAS_FMAT_FRID_Y_SAT = ["07-Apr", "08-Apr", "14-Apr", "15-Apr", "21-Apr",
                                     "22-Apr", "28-Apr", "29-Apr", "05-May", "06-May",
                                     "12-May", "13-May", "19-May", "20-May", "26-May",
                                     "27-May", "02-Jun", "03-Jun", "09-Jun", "10-Jun",
                                     "16-Jun", "17-Jun", "23-Jun", "24-Jun", "30-Jun"]


# Experimento 1: Se le permite viernes y sábado a Ingeniería

# Experimento 2: Se le prohibe sábado a Ingeniería
SABADOS_ABR = ["01-Apr", "08-Apr", "15-Apr", "22-Apr", "29-Apr"]
SABADOS_MAY = ["06-May", "13-May", "20-May", "27-May"]
SABADOS_JUN = ["03-Jun", "10-Jun", "17-Jun", "24-Jun"]
# Experimento 3: Se le prohibe viernes y sábado a Ingeniería
VIERNES_MAR = ["31-Mar"]
VIERNES_ABR = ["07-Apr", "14-Apr", "21-Apr", "28-Apr"]
VIERNES_MAY = ["05-May", "12-May", "19-May", "26-May"]
VIERNES_JUN = ["02-Jun", "09-Jun", "16-Jun", "23-Jun", "30-Jun"]

match NUM_EXPERIMENTO:
    case 1:
        pass
    case 2:
        FECHAS_PROHIBIDAS_ABRIL_GENERAL = FECHAS_PROHIBIDAS_ABRIL_GENERAL + SABADOS_ABR
        FECHAS_PROHIBIDAS_MAYO_GENERAL = FECHAS_PROHIBIDAS_MAYO_GENERAL + SABADOS_MAY
        FECHAS_PROHIBIDAS_JUNIO_GENERAL = FECHAS_PROHIBIDAS_JUNIO_GENERAL + SABADOS_JUN
    case 3:
        FECHAS_PROHIBIDAS_MARZO_GENERAL = FECHAS_PROHIBIDAS_MARZO_GENERAL + VIERNES_MAR
        FECHAS_PROHIBIDAS_ABRIL_GENERAL = FECHAS_PROHIBIDAS_ABRIL_GENERAL + \
            VIERNES_ABR + SABADOS_ABR
        FECHAS_PROHIBIDAS_MAYO_GENERAL = FECHAS_PROHIBIDAS_MAYO_GENERAL + \
            VIERNES_MAY + SABADOS_MAY
        FECHAS_PROHIBIDAS_JUNIO_GENERAL = FECHAS_PROHIBIDAS_JUNIO_GENERAL + \
            VIERNES_JUN + SABADOS_JUN


FECHAS_PROHIBIDAS_GENERAL = FECHAS_PROHIBIDAS_MARZO_GENERAL + \
    FECHAS_PROHIBIDAS_ABRIL_GENERAL + FECHAS_PROHIBIDAS_MAYO_GENERAL + \
    FECHAS_PROHIBIDAS_JUNIO_GENERAL

FECHAS_PROHIBIDAS_FMAT = list(
    set(FECHAS_PROHIBIDAS_GENERAL + FECHAS_PROHIBIDAS_FMAT_FRID_Y_SAT))

GRUPOS = [["MAT1620","FIS1514","IIC1103"],["MAT1620","ICE1514","IIC1103"],["MAT1630","FIS1523","MAT1640"],["MAT1630","IIQ1003","MAT1640"],
          ["MAT1630","ICM1003","MAT1640"],["EYP1113","FIS1533","ICS1513"],["EYP1113","IEE1533","ICS1513"],["FIS1514","FIS1523","FIS1533"],
          ["FIS1514","IIQ1003","FIS1533"],["FIS1514","ICM1003","FIS1533"],["FIS1514","FIS1523","IEE1533"],["FIS1514","IIQ1003","IEE1533"],
          ["FIS1514","ICM1003","IEE1533"],["IIC1253","IIC2233","IIC2343","MAT1610"],["MAT1610","MAT1203","QIM100E"],
          ["IIC1103","IIC1001","MAT1107","MAT1207"]]

DELTA_DIAS = 2

#Formato: si cursos todos coordinados: (curso (str), fecha (int), nr de prueba(int)) ¡La fecha debe ser en línea de tiempo real!
PRUEBAS_PREASIGNADAS = []

CURSOS_COORDINADOS = ["MAT1640","MAT1207","MAT1203","ICH1104","QIM200","EYP1113","MAT251I","MAT1107","FIS1514","ICE1514","ICS2613","MAT1630",
                      "ICS3213","FIS1533","MAT1610","MAT1620","MAT253I","ICM2503","QUO1112","MAT1605","FIS1523","IIQ1003","IIC3745",
                      "IIC1253","IIC1103","ICS1113","ICS113H","ICS1513","EYP2114","ICH3280","IEE2913","IEE3923","ICH3254","QIM100E","IIC2343",
                      "IEE3303"]

SEC_COORDINADAS = [["ICS3313","2","3"],["ICS3413","2","3"],["ICS2523","1","2"]]

CURSOS_3_IES = ["MAT1640_Coordinado - Macroseccion","MAT1630_Coordinado - Macroseccion","MAT1620_Coordinado - Macroseccion","MAT1610_Coordinado - Macroseccion",
                "MAT1203_Coordinado - Macroseccion","EYP1113_Coordinado - Macroseccion"]
#["EYP_MOD_MS1 - Macroseccion 1", "XN_MOD_MS1 - Macroseccion 1", "YF_MOD_MS1 - Macroseccion 1", "GCH_MOD_MS1 - Macroseccion 1", 
                #"ED_MOD_MS1 - Macroseccion 1", "WV_MOD_MS1 - Macroseccion 1"]

DIA_FECHA_RETIRO_CURSOS = "" #Se debe llevar a la línea temporal numérica

SEMANA_LICENCIATURA = 11

#Algunos parametros del modelo
DELTAMIN = 28
DELTAMAX = 63
VACANTES = 2000


#siglas fmat, fis y qim hardcodeadas en filtracion_archivos modulos_mod_dipre

INCLUIR_MAT = True
INCLUIR_FIS_Y_QIM = True

IDENTIFICADORES_FMAT = ["MAT1640", "MAT1630", "MAT1620", "MAT1610","MAT1207","EYP1113", "MAT1203"]
# IDENTIFICADORES_FMAT = ["EYP_MOD", "XN_MOD", "WV_MOD", "YF_MOD", "GCH_MOD", "ED_MOD"]

IDENTIFICADORES_FIS_Y_QIM = ["FIS1514", "FIS1523", "FIS1533", "QIM100E"]