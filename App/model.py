import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import arraylistiterator as it
from DISClib.ADT import map as m
from DISClib.Algorithms.Sorting import insertionsort as ins
import datetime
import random
from collections import defaultdict
import csv
import itertools
"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""
# -----------------------------------------------------
# API del TAD Catalogo de accidentes
def analyzer_context():
    analyzer_context = {"eventos":None,
                "index":None,
                "userid":None,
                "track_id":None,
                "instrumentalness":None,
                "liveness":None,
                "speechiness":None,
                "danceability":None,
                "valence":None,
                "loudness":None,
                "tempo":None,
                "acousticness":None,
                "energy":None,
                "artist_id":None,
                "created_at":None,
                "time_zone":None}
    analyzer_context["eventos"] = m.newMap(numelements=63400,
                                 prime=109345121, 
                                 maptype="CHAINING", 
                                 loadfactor=1, 
                                 comparefunction=comparer)
    analyzer_context["index"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_context["artist_id"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_context["userid"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_context["track_id"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_context["created_at"]=om.newMap(omaptype="RBT",
                                comparefunction=compareTime)
    analyzer_context["instrumentalness"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLat)
    analyzer_context["liveness"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["speechiness"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["danceability"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["valence"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["loudness"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["tempo"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["acousticness"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["energy"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareLiv)
    analyzer_context["time_zone"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareZone)
                
    return analyzer_context
def analyzer_usertrack():
    analyzer_usertrack={"usuarios":None,
                        "user_id":None,
                        "index":None,
                        "track_id":None,
                        "hashtag":None,
                        "created_at":None}
    analyzer_usertrack["usuarios"] = m.newMap(numelements=87900,
                                 prime=109345121, 
                                 maptype="CHAINING", 
                                 loadfactor=1, 
                                 comparefunction=comparer2)
    analyzer_usertrack["user_id"]=om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_usertrack["index"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_usertrack["track_id"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_usertrack["hashtag"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareZone)
    analyzer_usertrack["created_at"]=om.newMap(omaptype="RBT",
                                comparefunction=compareTime)
    return analyzer_usertrack
def analyzer_sentiment():
    analyzer_sentiment={"sentimientos":None,
                        "index":None,
                        "vader_min":None,
                        "vader_max":None,
                        "vader_avg":None}
    analyzer_sentiment["sentimientos"]=m.newMap(numelements=5292,
                                 prime=109345121, 
                                 maptype="CHAINING", 
                                 loadfactor=1, 
                                 comparefunction=comparer2)
    analyzer_sentiment["index"]=om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    analyzer_sentiment["vader_min"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareZone)
    analyzer_sentiment["vader_max"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareZone)
    analyzer_sentiment["vader_avg"]=om.newMap(omaptype="RBT",
                                    comparefunction=compareZone)
    return analyzer_sentiment
# -----------------------------------------------------
def fecha_convertidor(dato):
    crimedate = datetime.datetime.strptime(dato, '%Y-%m-%d %H:%M:%S')
    return crimedate.date()
def fecha_convertidor_consultas(dato):
    crimedate = datetime.datetime.strptime(dato, '%Y-%m-%d')
    return crimedate.date()
def hora_convertidor(dato):
    crimetime=datetime.datetime.strptime(dato,'%Y-%m-%d %H:%M:%S')
    return crimetime.time()
def hora_convertidor_consultas(dato):
    crimetime=datetime.datetime.strptime(dato,'%H:%M:%S')
    return crimetime.time()
# Funciones para agregar informacion al catalogo

def cargaridcrimen(analyzer_context, crimen):
    listac = analyzer_context["eventos"]
    index = analyzer_context["index"]
    inst=analyzer_context["instrumentalness"]
    liv=analyzer_context["liveness"]
    spec=analyzer_context["speechiness"]
    dance=analyzer_context["danceability"]
    val=analyzer_context["valence"]
    loud=analyzer_context["loudness"]
    temp=analyzer_context["tempo"]
    aco=analyzer_context["acousticness"]
    eng=analyzer_context["energy"]
    hora=analyzer_context["created_at"]
    horas=hora_convertidor(crimen["created_at"])
    fecha = fecha_convertidor(crimen["created_at"])
    instrumentalness=float(crimen["instrumentalness"])
    liveness=float(crimen["liveness"])
    speechiness=float(crimen["speechiness"])
    danceability=float(crimen["danceability"])
    valence=float(crimen["valence"])
    loudness=float(crimen["loudness"])
    tempo=float(crimen["tempo"])
    acousticness=float(crimen["acousticness"])
    energy=float(crimen["energy"])
    m.put(listac, crimen["id"], crimen)
    if om.contains(index, fecha)==True and om.contains(hora,horas)==True and om.contains(liv,liveness)==True and om.contains(inst,instrumentalness)==True and om.contains(spec,speechiness)==True and om.contains(dance,danceability)==True and om.contains(val,valence)==True and om.contains(loud,loudness)==True and om.contains(temp,tempo)==True and om.contains(aco,acousticness)==True and om.contains(eng,energy)==True:
        agregarid(index, crimen, fecha)
        agregarid_2(hora,crimen,horas)
        agregarid_3(inst,crimen,instrumentalness)
        agregarid_4(liv,crimen,liveness)
        agregarid_5(spec,crimen,speechiness)
        agregarid_6(dance,crimen,danceability)
        agregarid_7(val,crimen,valence)
        agregarid_8(loud,crimen,loudness)
        agregarid_9(temp,crimen,tempo)
        agregarid_10(aco,crimen,acousticness)
        agregarid_11(eng,crimen,energy)
        
    else:
        agregarfecha(index, crimen, fecha) 
        agregarhora(hora,crimen,horas)
        agregar_instrumentalness(inst,crimen,instrumentalness)
        agregar_liveness(liv,crimen,liveness)
        agregar_speechiness(spec,crimen,speechiness)
        agregar_danceability(dance,crimen,danceability)
        agregar_valence(val,crimen,valence)
        agregar_loudness(loud,crimen,loudness)
        agregar_tempo(temp,crimen,tempo)
        agregar_acousticness(aco,crimen,acousticness)
        agregar_energy(eng,crimen,energy)
def agregarid(index, crimen, fecha):
    a = om.get(index, fecha)
    b = me.getValue(a)
    lt.addLast(b, crimen["id"])
def agregarid_2(index,crimen,hora):
    a=om.get(index,hora)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_3(index,crimen,instrumentalness):
    a=om.get(index,instrumentalness)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_4(index,crimen,liveness):
    a=om.get(index,liveness)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_5(index,crimen,speechiness):
    a=om.get(index,speechiness)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_6(index,crimen,danceability):
    a=om.get(index,danceability)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_7(index,crimen,valence):
    a=om.get(index,valence)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_8(index,crimen,loudness):
    a=om.get(index,loudness)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_9(index,crimen,tempo):
    a=om.get(index,tempo)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_10(index,crimen,acousticness):
    a=om.get(index,acousticness)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarid_11(index,crimen,energy):
    a=om.get(index,energy)
    b=me.getValue(a)
    lt.addLast(b,crimen["id"])
def agregarfecha(index, crimen, fecha):
    N = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N, crimen["id"])
    om.put(index, fecha, N)
def agregarhora(index,crimen,hora):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,hora,N)
def agregar_instrumentalness(index,crimen,instrumentalness):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,instrumentalness,N)
def agregar_liveness(index,crimen,liveness):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,liveness,N)
def agregar_speechiness(index,crimen,speechiness):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,speechiness,N)
def agregar_danceability(index,crimen,danceability):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,danceability,N)
def agregar_valence(index,crimen,valence):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,valence,N)
def agregar_loudness(index,crimen,loudness):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,loudness,N)
def agregar_tempo(index,crimen,tempo):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,tempo,N)
def agregar_acousticness(index,crimen,acousticness):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,acousticness,N)
def agregar_energy(index,crimen,energy):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["id"])
    om.put(index,energy,N)
#--------------------------------------------2-------------------------------------
def cargaridcrimen_2(analyzer_usertrack, crimen):
    listac = analyzer_usertrack["usuarios"]
    user_id=analyzer_usertrack["user_id"]
    index = analyzer_usertrack["index"]
    hora=analyzer_usertrack["created_at"]
    horas=hora_convertidor(crimen["created_at"])
    fecha = fecha_convertidor(crimen["created_at"])
    m.put(listac, crimen["user_id"], crimen)
    if om.contains(index, fecha)==True and om.contains(hora,horas)==True:
        agregarid_fecha(index, crimen, fecha)
        agregarid_2_hora(hora,crimen,horas)
    else:
        agregarfecha_2(index, crimen, fecha) 
        agregarhora_2(hora,crimen,horas)
def agregarid_fecha(index,crimen,fecha):
    a = om.get(index, fecha)
    b = me.getValue(a)
    lt.addLast(b, crimen["user_id"])
def agregarid_2_hora(index,crimen,hora):
    a=om.get(index,hora)
    b=me.getValue(a)
    lt.addLast(b,crimen["user_id"])
def agregarfecha_2(index, crimen, fecha):
    N = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N, crimen["user_id"])
    om.put(index, fecha, N)
def agregarhora_2(index,crimen,hora):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["user_id"])
    om.put(index,hora,N)
#--------------------------------------3---------------------
def cargaridcrimen_3(analyzer_sentiment, crimen):
    listac = analyzer_sentiment["sentimientos"]
    minimo=analyzer_sentiment["vader_min"]
    maximo=analyzer_sentiment["vader_max"]
    average=analyzer_sentiment["vader_avg"]
    vader_min=crimen[" vader_min"]
    vader_max=crimen[" vader_max"]
    vader_avg=crimen["vader_avg"]
    m.put(listac, crimen["hashtag"], crimen)
    if om.contains(minimo,vader_min)==True and om.contains(maximo,vader_max)==True and om.contains(average,vader_avg)==True:
        agregarid_min(minimo,crimen,vader_min)
        agregarid_max(maximo,crimen,vader_max)
        agregarid_avg(average,crimen,vader_avg)
    else:
        agregar_vader_min(minimo,crimen,vader_min)
        agregar_vader_max(maximo,crimen,vader_max)
        agregar_vader_avg(average,crimen,vader_avg)
def agregarid_min(index,crimen,vader_min):
    a=om.get(index,vader_min)
    b=me.getValue(a)
    lt.addLast(b,crimen["hashtag"])
def agregarid_max(index,crimen,vader_max):
    a=om.get(index,vader_max)
    b=me.getValue(a)
    lt.addLast(b,crimen["hashtag"])
def agregarid_avg(index,crimen,vader_avg):
    a=om.get(index,vader_avg)
    b=me.getValue(a)
    lt.addLast(b,crimen["hashtag"])
def agregar_vader_min(index,crimen,vader_min):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["hashtag"])
    om.put(index,vader_min,N)
def agregar_vader_max(index,crimen,vader_max):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["hashtag"])
    om.put(index,vader_max,N)
def agregar_vader_avg(index,crimen,vader_avg):
    N=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N,crimen["hashtag"])
    om.put(index,vader_avg,N)
# ==============================
# REQUERIMIENTOS 
def Requerimiento_1(analyzer_context,caracteristica,valor_minimo,valor_maximo):
    resp=[]
    if caracteristica in "instrumentalidad" or caracteristica in "instrumentalness":
        llaves=om.keys(analyzer_context["instrumentalness"],valor_minimo,valor_maximo)
    elif caracteristica in "vivacidad" or caracteristica in "liveness":
         llaves=om.keys(analyzer_context["liveness"],valor_minimo,valor_maximo)
    elif caracteristica in "speechiness":
        llaves=om.keys(analyzer_context["speechiness"],valor_minimo,valor_maximo)
    elif caracteristica in "bailabilidad" or caracteristica in "danceability":
        llaves=om.keys(analyzer_context["danceability"],valor_minimo,valor_maximo)
    elif caracteristica in "valencia" or caracteristica in "valence":
        llaves=om.keys(analyzer_context["valence"],valor_minimo,valor_maximo)
    elif caracteristica in "volumen" or caracteristica in "loudness":
        llaves=om.keys(analyzer_context["loudness"],valor_minimo,valor_maximo)
    elif caracteristica in "tempo":
        llaves=om.keys(analyzer_context["tempo"],valor_minimo,valor_maximo)
    elif caracteristica in "acústica" or caracteristica in "acousticness":
        llaves=om.keys(analyzer_context["acousticness"],valor_minimo,valor_maximo)
    else:
        resp=None
    if resp!=None:
        iterador = llaves ['first']
        fecha_mayor = iterador ['info'] 
        crimenesmas = me.getValue(om.get (analyzer_context[caracteristica], fecha_mayor))
        val=[]
        users=[]
        cmas = it.newIterator(crimenesmas)    
        while it.hasNext(cmas):
            n = it.next(cmas)        
            A =     m.get(analyzer_context["eventos"], n)        
        while iterador['next'] != None:        
            iterador = iterador ['next']
            llave = iterador ['info']
            crimenes = me.getValue(om.get (analyzer_context[caracteristica], llave))
            c = it.newIterator(crimenes)
            while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                val.append(B["id"])   
                users.append(B["artist_id"])
        unicos=set(users)
        resp=(len(val),len(unicos))
    return resp
#-----------------------------------------------------------------------------------
def Requerimiento_2(analyzer_context,enery_min,energy_max,dance_min,dance_max):
    energia=om.keys(analyzer_context["energy"],enery_min,energy_max)
    dance=om.keys(analyzer_context["danceability"],dance_min,dance_max)
    iterador = energia['first']
    fecha_mayor = iterador ['info'] 
    tracks=[]
    energia=[]
    while iterador['next'] != None:        
        iterador = iterador ['next']
        llave = iterador ['info']
        crimenes = me.getValue(om.get (analyzer_context['energy'], llave))
        c = it.newIterator(crimenes)
        while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                tracks.append(B["track_id"])
                energia.append(B["energy"])
    iterador_2=dance["first"]
    informacion=iterador_2["info"]
    tracks_2=[]
    baile=[]
    while iterador_2["next"]!=None:
        iterador_2=iterador_2["next"]
        llave_2=iterador_2["info"]
        crimenes2 = me.getValue(om.get (analyzer_context['danceability'], llave_2))
        c = it.newIterator(crimenes2)
        while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                tracks_2.append(B["track_id"])
                baile.append(B["danceability"])
    if len(tracks)==0 or len(tracks_2)==0:
        resp=None
    else:  
        list_3=[]           
        for z in tracks:
            for b in tracks_2:
                if z==b:
                    list_3.append(z)
        unicos=set(list_3)
        rand=random.sample(unicos, 5)
        resp=[]
        for i in rand:
            resp.append([i,energia[tracks.index(i)],baile[tracks_2.index(i)]])
    return (resp,len(unicos))
#--------------------------------------------------------------------------------------
def Requerimiento_3(analyzer_context,inst_min,inst_max,temp_min,temp_max):
    instrumentalness=om.keys(analyzer_context["instrumentalness"],inst_min,inst_max)
    tempo=om.keys(analyzer_context["tempo"],temp_min,temp_max)
    iterador = instrumentalness['first']
    fecha_mayor = iterador ['info'] 
    tracks=[]
    energia=[]
    while iterador['next'] != None:        
        iterador = iterador ['next']
        llave = iterador ['info']
        crimenes = me.getValue(om.get (analyzer_context['instrumentalness'], llave))
        c = it.newIterator(crimenes)
        while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                tracks.append(B["track_id"])
                energia.append(B["instrumentalness"])
    iterador_2=tempo["first"]
    informacion=iterador_2["info"]
    tracks_2=[]
    baile=[]
    while iterador_2["next"]!=None:
        iterador_2=iterador_2["next"]
        llave_2=iterador_2["info"]
        crimenes2 = me.getValue(om.get (analyzer_context['tempo'], llave_2))
        c = it.newIterator(crimenes2)
        while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                tracks_2.append(B["track_id"])
                baile.append(B["tempo"])
    if len(tracks)==0 or len(tracks_2)==0:
        resp=None
    else:  
        list_3=[]           
        for z in tracks:
            for b in tracks_2:
                if z==b:
                    list_3.append(z)
        unicos=set(list_3)
        rand=random.sample(unicos, 5)
        resp=[]
        for i in rand:
            resp.append([i,energia[tracks.index(i)],baile[tracks_2.index(i)]])
    return (resp,len(unicos))
#---------------------------------------------------------------------------------------
def Requerimiento_4(analyzer_context,opcion,tempo_min,tempo_max,lista):
    if opcion=="True":
        tempos=[]
        for i in lista:
            if i in "Reggae":
                tempos.append((60,90))
            elif i in "Down-tempo":
                tempos.append((70,100)) 
            elif i in "Chill-out":
                tempos.append((90,120))
            elif i in "Hip-hop":
                tempos.append((85,115))
            elif i in "Jazz and Funk ":
                tempos.append((120,125))
            elif i in "Pop":
                tempos.append((100,130))
            elif i in "R&B":
                tempos.append((60,80))
            elif i in "Rock":
                tempos.append((110,140))
            elif i in "Metal":
                tempos.append((100,160))
            else:
                tempos.append((tempo_min,tempo_max))
            tracks=[]
        resp=[]
        a=[]
        for z in tempos:
            tracks.append(analizador_tempos(analyzer_context,z[0],z[1]))
        for i in tracks:
            resp.append(i[0][:11])
            a.append((i[1],len(i[0])))
    else:
        tempos=[]
        for i in lista:
            if i in "Reggae":
                tempos.append((60,90))
            elif i in "Down-tempo":
                tempos.append((70,100)) 
            elif i in "Chill-out":
                tempos.append((90,120))
            elif i in "Hip-hop":
                tempos.append((85,115))
            elif i in "Jazz and Funk ":
                tempos.append((120,125))
            elif i in "Pop":
                tempos.append((100,130))
            elif i in "R&B":
                tempos.append((60,80))
            elif i in "Rock":
                tempos.append((110,140))
            else:
                tempos.append((100,160))
        tracks=[]
        resp=[]
        a=[]
        for z in tempos:
            tracks.append(analizador_tempos(analyzer_context,z[0],z[1]))
        for i in tracks:
            resp.append(i[0][:11])
            a.append((i[1],len(i[0])))
    return (resp,a)
def analizador_tempos(analyzer_context,tempo_min,tempo_max):
    tempo=om.keys(analyzer_context["tempo"],tempo_min,tempo_max)
    iterador_2=tempo["first"]
    informacion=iterador_2["info"]
    usuarios_2=[]
    tempos=[]
    while iterador_2["next"]!=None:
        iterador_2=iterador_2["next"]
        llave_2=iterador_2["info"]
        crimenes2 = me.getValue(om.get (analyzer_context['tempo'], llave_2))
        c = it.newIterator(crimenes2)
        while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                usuarios_2.append(B["artist_id"])
                tempos.append(B["track_id"])
    unicos=list(set(usuarios_2))
    return (unicos,len(tempos))
#-------------------------------------------------------------------
def Requerimiento_5(hora_min,hora_max,analyzer_context):
    hora_menor=hora_convertidor_consultas(hora_min)
    hora_mayor=hora_convertidor_consultas(hora_max)
    llaves=om.keys(analyzer_context["created_at"],hora_menor,hora_mayor)
    iterador_2=llaves["first"]
    informacion=iterador_2["info"]
    usuarios_2=[]
    tempos=[]
    while iterador_2["next"]!=None:
        iterador_2=iterador_2["next"]
        llave_2=iterador_2["info"]
        crimenes2 = me.getValue(om.get (analyzer_context['created_at'], llave_2))
        c = it.newIterator(crimenes2)
        while it.hasNext(c):
                n = it.next(c)        
                A = m.get(analyzer_context["eventos"], n)        
                B = me.getValue(A)
                usuarios_2.append(float(B["tempo"]))
                tempos.append(str(B["track_id"]))
    géneros=[]
    for i in usuarios_2:
        if i>=60 and i<=90:
            géneros.append("Reggae")
        if i>=70 and i<=100:
            géneros.append("Down-tempo")
        if i>=90 and i<=120:
            géneros.append("Chill-out")
        if i>=85 and i<=115:
            géneros.append("Hip-hop")
        if i>=120 and i<=125:
            géneros.append("Jazz and Funk")
        if i>=100 and i<=130:
            géneros.append("Pop")
        if i>=60 and i<=80:
            géneros.append("R&B")
        if i>=110 and  i<=140:
            géneros.append("Rock")
        if i>=100 and i<=160:
            géneros.append("Metal")
    h = defaultdict(list)
    for k, v in zip(géneros, tempos):
        h[k].append(v) 
    x={k: v for k, v in sorted(h.items(), key=lambda item: len(item[1]),reverse=True)} 
    longi=[] 
    for i in x:
        longi.append(len(h[i]))
    return (x,longi)
    
def Requerimiento_5_parte_2(analyzer_usertrack,Requerimiento_5,analyzer_sentiment):
    clave=None
    contador=0
    for i in Requerimiento_5[0]:
         if contador==0:
             clave=i
             contador+=1
    tracks=Requerimiento_5[0][clave]
    a=[]
    b=[]
    for i in analyzer_usertrack:
        for k,v in i.items():
            if k=="track_id":
                a.append(v)
            elif k=="hashtag":
                b.append(v)
    c=[]
    for z in tracks:
        c.append([i for i, x in enumerate(a) if x == z])
    flat_list = []
    for sublist in c:
        for item in sublist:
            flat_list.append(item)
    tracks_2=[]
    hashtag=[]
    for i in flat_list:
        tracks_2.append(a[i])
        hashtag.append(b[i])
    valores=[]
    o=[]
    for i in analyzer_sentiment:
        for k,v in i.items():
            if k=="hashtag":
                o.append(v)
            elif k=="vader_avg":
                valores.append(v)
    diccionario=dict(zip(o,valores))
    diccionario_llaves=list(diccionario.keys())
    valores_a_encontrar=[]
    for z in hashtag:
        valores_a_encontrar.append([i for i, x in enumerate(diccionario_llaves) if x in z])
    flat=[]
    for sublist in valores_a_encontrar:
        for item in sublist:
            flat.append(item)
    flat_2=[]
    for i in flat:
        if valores[i]=="":
            flat_2.append(0)
        else:
            flat_2.append(float(valores[i]))
    h = defaultdict(list)
    for k, v in zip(tracks_2,flat_2):
        h[k].append(v)
    x={k: v for k, v in sorted(h.items(), key=lambda item: len(item[1]),reverse=True)} 
    d=dict(itertools.islice(x.items(),10))
    longi=[] 
    for i in d:
        longi.append(len(d[i]))
    for key in d: 
        d[key] = round(sum(d[key])/len(d[key]),2)
    unicos=list(set(tracks))
    return (d,longi,len(unicos))
                
# ==============================
# ==============================
# Funciones de Comparacion
# ==============================
def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def compareTime(time1,time2):
    if (time1==time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1

def comparer(keyname, value):
    entry = me.getKey(value)
    if (keyname == entry):
        return 0
    elif (keyname > entry):
        return 1
    else:
        return -1
def comparer2(keyname, value):
    entry = me.getKey(value)
    if (keyname == entry):
        return 0
    elif (keyname > entry):
        return 1
    else:
        return -1
def compareLat(lat1,lat2):
    if (float(lat1)==float(lat2)):
        return 0
    elif (float(lat1) > float(lat2)):
        return 1
    else:
        return -1
def compareLiv(lat1,lat2):
    if (float(lat1)==float(lat2)):
        return 0
    elif (float(lat1) > float(lat2)):
        return 1
    else:
        return -1
def compareLog(lng1,lng2):
    if (lng1==lng2):
        return 0
    elif (lng1>lng2):
        return 1
    else:
        return -1
def compareZone(time1,time2):
    if (time1==time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1
def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['index'])
def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['index'])
def cargarCategorias():
    vfile = cf.data_dir + "user_track_hashtag_timestamp-small.csv"
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    cat = []
    for line in reader:
        cat.append(dict(line))
    return cat
def cargarCategorias1():
    vfile = cf.data_dir + "sentiment_values.csv"
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    cat = []
    for line in reader:
        cat.append(dict(line))
    return cat
