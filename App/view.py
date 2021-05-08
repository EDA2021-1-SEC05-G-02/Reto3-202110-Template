import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylistiterator as it
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
from App import controller
assert config
crimefile = "context_content_features-large.csv"
crimefile_2="user_track_hashtag_timestamp-large.csv"
crimefile_3="sentiment_values.csv"
"""INTENTEN CON EL GRANDE"""

# _________________
#  Menu principal
# _________________


def printMenu():
    print("\n")
    print("***************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de música")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("0- Salir")
    print("***************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # analyzer es el controlador que se usará de acá en adelante
        analyzer = controller.init()
        analyzer_2=controller.init_2()
        analyzer_3=controller.cargarCategorias_2()
        analyzer_4=controller.cargarCategorias_1()
        print("\nAnalizador cargado.")

    elif int(inputs[0]) == 2:
        print("\nCargando información de eventos y usuarios ....")
        controller.loadData(analyzer, crimefile)
        controller.loadData_2(analyzer_2,crimefile_2)
        print("\nInformacion caragada exitosamente")
        print("Se cargaron",m.size(analyzer["eventos"]),"eventos.")
        print("Se cargaron",m.size(analyzer_2["usuarios"]),"artistas únicos.")

    elif int(inputs[0]) == 3:
        caracteristica=input("Deme la característica: ")
        caracteristica.lower()
        valor_minimo=float(input("Valor mínimo: "))
        valor_maximo=float(input("Valor máximo: "))
        Requerimiento_1=controller.Requerimiento_1(analyzer,caracteristica,valor_minimo,valor_maximo)
        if Requerimiento_1==None:
            print("Característica errónea")
        else:
            print(caracteristica+" se encuentra entre "+str(valor_minimo)+" y "+str(valor_maximo))
            print("Total de reproducciones: "+str(Requerimiento_1[0])+" Total de artistas únicos: "+str(Requerimiento_1[1]))

    elif int(inputs[0]) == 4:
        energy_min=float(input("Energía mínima: "))
        energy_max=float(input("Energía máxima: "))
        dance_min=float(input("Bailabilidad mínima: "))
        dance_max=float(input("Bailabilidad máxima: "))
        Requerimiento_2=controller.Requerimiento_2(analyzer,energy_min,energy_max,dance_min,dance_max)
        print("Energy es entre "+str(energy_min)+" y "+str(energy_max))
        print("Danceability es entre "+str(dance_min)+" y "+str(dance_max))
        print("Total de pistas únicas en eventos: "+str(Requerimiento_2[1]))
        cont=1
        if Requerimiento_2!=None:
            for i in Requerimiento_2[0]:
                print("Track"+str(cont)+": "+str(i[0])+" con una energía de "+str(i[1])+" y una danceability de "+str(i[2]))
                cont+=1
        else:
            print("Revise los valores agregados")
        
    elif int(inputs[0]) == 5:
        inst_min=float(input("Deme instrumentalidad mínima: "))
        inst_max=float(input("Deme instrumentalidad máxima: "))
        temp_min=float(input("Deme tempo mínimo: "))
        temp_max=float(input("Deme tempo máximo: "))
        Requerimiento_3=controller.Requerimiento_3(analyzer,inst_min,inst_max,temp_min,temp_max)
        print("Instrumentalidad es entre "+str(inst_min)+" y "+str(inst_max))
        print("Tempo es entre "+str(temp_min)+" y "+str(temp_max))
        print("Total de pistas únicas en eventos: "+str(Requerimiento_3[1]))
        cont=1
        if Requerimiento_3!=None:
            for i in Requerimiento_3[0]:
                print("Track"+str(cont)+": "+str(i[0])+" con una instrumentalidad de "+str(i[1])+" y un tempo de "+str(i[2]))
                cont+=1
        else:
            print("Revise los valores agregados")

    elif int (inputs [0])==6:
        opcion=str(input("Digite True si desea agregar un género nuevo: "))
        lst = []
        if opcion in "True":
            nombre=input("Digite el nombre del género a agregar: ")
            tempo_min=float(input("Ingrese el valor del tempo menor: "))
            tempo_mayor=float(input("Ingrese el valor del tempo mayor: "))
            n = int(input("Ingrese el número de géneros a mostar por pantalla : "))
            for i in range(0, n):
                print("Género a buscar: ( Reggae, Down-tempo, Chill-out, Hip-hop,Jazz and Funk,Pop,R&B,Rock,Metal")
                ele = (input("Deme el nombre del género a consultar: "))
                lst.append(ele)
            lst.append(nombre)
        else:
            n = int(input("Ingrese el número de géneros a mostar por pantalla : "))
            nombre=None
            tempo_min=None
            tempo_mayor=None
            for i in range(0, n):
                print("Género a buscar: ( Reggae, Down-tempo, Chill-out, Hip-hop,Jazz and Funk,Pop,R&B,Rock,Metal")
                ele = (input("Deme el nombre del género a consultar: "))
                lst.append(ele)
        cont=0
        contador=0
        Requerimiento_4=controller.Requerimiento_4(analyzer,opcion,tempo_min,tempo_mayor,lst)
        while cont<len(lst):
            for i in Requerimiento_4[0]:
                if contador==0:
                    print("====================="+lst[cont].upper()+"==================")
                    print(lst[cont]+" reproducciones: "+str(Requerimiento_4[1][cont][0])+" con "+str(Requerimiento_4 [1][cont][1])+" artistas únicos")
                    contador+=1
                elif contador==11:
                    contador=0
                    cont+=1
                else:
                    print("Artista"+str(contador)+": "+str(i[contador]))
                    contador+=1
                    
    elif int(inputs[0])==7:
        date=str(input("Deme hora inicial: "))
        date2=str(input("Deme hora final: "))
        Requerimiento_5=controller.Requerimiento_5(date,date2,analyzer)
        print("Hay un total de "+str(sum(Requerimiento_5[1]))+" reproducciones entre "+str(date)+" y las "+str(date2))
        print("====================== REPRODUCCIONES ORGANIZADAS DE GÉNEROS ======================")
        contador=0
        for i in Requerimiento_5[0]:
            print("TOP "+str(contador+1)+" "+str(i)+" con "+str(Requerimiento_5[1][contador]))
            contador+=1
        lista_llaves=list(Requerimiento_5[0].keys())
        print("El género TOP es "+str(lista_llaves[0])+" con "+str(Requerimiento_5[1][0])+" reproducciones.")
        Parte_2=controller.Requerimiento_5_parte_2(analyzer_4,Requerimiento_5,analyzer_3)
        cont=0
        print("El género TOP tiene "+str(Parte_2[2])+" canciones únicas")
        print("LAS 10 PRIMERAS CANCIONES SON")
        for i in Parte_2[0]:
            print("TOP "+str(cont+1)+" Canción: "+str(i)+" con "+str(Parte_2[1][cont])+" hashtags repetidos incluidos y un vader promedio de: "+str(Parte_2[0][i]))
            cont+=1
    else:
        sys.exit(0)
sys.exit(0)
