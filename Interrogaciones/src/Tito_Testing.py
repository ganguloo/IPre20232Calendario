from filtracion_archivos import modulos_mod_dipre,cursos_con_ies
from parametros.parametros import PATH_CURSOS_IES,PATH_LISTADO_NRC
import pandas as pd
from parametros.cursos_ies import CONJUNTO_INTERROGACIONES


print(len(CONJUNTO_INTERROGACIONES["IIC3103-1"]))
'''cursos_ing_ies = cursos_con_ies.cursos_con_pruebas(PATH_CURSOS_IES)
out = (modulos_mod_dipre.cursos_mod_dipre(PATH_LISTADO_NRC, cursos_ing_ies)).to_pandas()
out = out.values.tolist()
file = open("output_test_tito.txt", "w")
for i in out :
    for j in i:
        file.write(str(j))
    file.write("\n")'''