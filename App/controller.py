import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# _________________
#  Inicializacion del catalogo
# _________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    Analyzer = model.analyzer_context()
    return Analyzer
def init_2():
    analyzer_2=model.analyzer_usertrack()
    return analyzer_2
def init_3():
    analyzer_3=model.analyzer_sentiment()
    return analyzer_3
# _________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# _________________

def loadData(analyzer, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile = cf.data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        model.cargaridcrimen(analyzer, crime)

    return analyzer
def loadData_2(analyzer_2, crimesfile_2):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile_2 = cf.data_dir + crimesfile_2
    input_file = csv.DictReader(open(crimesfile_2, encoding="utf-8"),
                                delimiter=",")
    for crimen in input_file:
        model.cargaridcrimen_2(analyzer_2,crimen)

    return analyzer_2
def loadData_3(analyzer_3, crimesfile_3):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile_3 = cf.data_dir + crimesfile_3
    input_file = csv.DictReader(open(crimesfile_3, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        model.cargaridcrimen_3(analyzer_3, crime)

    return analyzer_3
# ____________________________
def Requerimiento_1(analyzer_context,caracteristica,valor_minimo,valor_maximo):
    return model.Requerimiento_1(analyzer_context,caracteristica,valor_minimo,valor_maximo)
def Requerimiento_2(analyzer_context,enery_min,energy_max,dance_min,dance_max):
    return model.Requerimiento_2(analyzer_context,enery_min,energy_max,dance_min,dance_max)
def Requerimiento_3(analyzer_context,inst_min,inst_max,temp_min,temp_max):
    return model.Requerimiento_3(analyzer_context,inst_min,inst_max,temp_min,temp_max)
def Requerimiento_4(analyzer_context,opcion,temp_min,temp_max,lista):
    return model.Requerimiento_4(analyzer_context,opcion,temp_min,temp_max,lista)
def Requerimiento_5(hora_min,hora_max,analyzer_context):
    return model.Requerimiento_5(hora_min,hora_max,analyzer_context)
def Requerimiento_5_parte_2(analyzer_usertrack,Requerimiento_5,analyzer_sentiment):
    return model.Requerimiento_5_parte_2(analyzer_usertrack,Requerimiento_5,analyzer_sentiment)
def cargarCategorias_1():
    return model.cargarCategorias()
def cargarCategorias_2():
    return model.cargarCategorias1()