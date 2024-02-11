from os import system
import json
import modulo.validate as validate
import main
from .data import notas, camper




def guardarNotasModulo():
    bandera=True
    while (bandera):
        id=input("Indique id del camper\n")
        with open("modulo/storage/camper.json") as f:
            campers=json.loads(f.read())
            for camper in campers:
                if id==camper["Id"] and camper["Estado"]=="Aprobado":
                    infoNota = {
            "Modulo": int(),
            "Id":"",
            "Teorica":"",
            "Practica":"",
            "Trabajos":""
        }
                    infoNota["Modulo"]=int(input("¿En qué modulo desea guardar las notas?"))
                    infoNota["Id"]=id
                    bandera1=True
                    while (bandera1):
                        teorica = input("Prueba teorica: ")
                        if teorica.isnumeric():
                            infoNota["Teorica"]=teorica
                            bandera1=False
                    bandera1=True
                    while (bandera1):        
                        practica=input("Prueba practica: ")
                        if practica.isnumeric():
                            infoNota["Practica"]=practica
                            bandera1=False
                    bandera1=True
                    while (bandera1):
                        trabajos=input("trabajos: ")
                        if trabajos.isnumeric():
                            infoNota["Trabajos"]=trabajos
                            bandera1=False
                    with open("modulo/storage/notas.json") as f:
                        notas = json.load(f)
                        notas.append(infoNota)
                    with open("modulo/storage/notas.json", "w") as f:
                        data=json.dumps(notas, indent=4)
                        f.write(data)
                        f.close()
                        system("clear")
                elif id==camper["Id"] and camper["Estado"]=="Inscrito":
                    infoNota={
                        "Id": "",
                        "Teorica": "",
                        "Practica": "",
                    }
                    infoNota["Id"]=id
                    bandera1=True
                    while (bandera1):
                        teorica = input("Prueba teorica: ")
                        if teorica.isnumeric():
                            infoNota["Teorica"]=teorica
                            bandera1=False
                    bandera1=True
                    while (bandera1):        
                        practica=input("Prueba practica: ")
                        if practica.isnumeric():
                            infoNota["Practica"]=practica
                            bandera1=False
                    if (int(practica)+int(teorica))/2 >= 60:
                        camper["Estado"]="Aprobado"
                    else:
                        camper["Estado"]="Filtrado"
                    with open("modulo/storage/camper.json","w") as f:
                        dataCamper=json.dumps(campers, indent=4)
                        f.write(dataCamper)
                        f.close()


                    with open("modulo/storage/preNotas.json") as f:
                        notas = json.load(f)
                        notas.append(infoNota)
                    with open("modulo/storage/preNotas.json", "w") as f:
                        data=json.dumps(notas, indent=4)
                        f.write(data)
                        f.close()
                        system("clear")
        bandera=False
    return "Guardado"




def buscar():
    while True:
        id = int(input("Indique la identificacion del camper\n"))
        with open("modulo/storage/notas.json","r") as f:
            data = json.loads(f.read())
            f.close()
            for datos in data:
                if id==datos["Id"]:
                    print(datos)
        print(datos)
        with open("modulo/storage/camper.json","r") as f1:
            data1 = json.loads(f1.read())
            f1.close()
            for datos1 in data1:
                if id==datos1["Id"]:
                    print(datos1)
            print(f"""
    ______________________________
    ______________________________
    Nombre: {datos1.get('Nombre')}      
    Apellido: {datos1.get('Apellido')}
    Teorica: {datos.get('Teorica')}
    Practica: {datos.get('Practica')}
    Trabajos: {datos.get('Trabajos')}  
    ______________________________
    ______________________________                  
                """)
        bandera=True
        while(bandera):
            print("\t1. Seguir Buscando")
            print("\t2. Salir")
            opc=input()
            if opc.isnumeric():
                bandera=False
        if opc=="1":
            buscar()
        elif opc=="2":
            main.menuPrincipal()#Corregir codigo
        else:
            validate.noValid()
                
    return "Notas Cargadas"

# def actualizar():
#     id = int(input("Identificación del camper:\n"))
#     with open("modulo/storage/notas.json") as f:


def aprobados():
    with open("modulo/storage/camper.json") as f:
        listaCamper =json.loads(f.read())
        f.close()
    with open("modulo/storage/notas.json") as f:
        data = json.loads(f.read())
        f.close()
        for datos in data:
            if ((int(datos["Teorica"])*0.3)+(int(datos["Practica"]))*0.6)+(int(datos["Trabajos"])*0.1) >= 60:
                aprobados = datos
                id=aprobados["Id"]
                #print(aprobados)
                for camper in listaCamper:
                    if id==camper["Id"]:
                        print(f"""
Id: {camper.get('Id')}
Nombre: {camper.get('Nombre')}
Apellido: {camper.get('Apellido')}
Teorica: {aprobados.get('Teorica')}
Practica: {aprobados.get('Practica')}
Trabajos: {aprobados.get('Trabajos')}
                              """)
    return "Lista de aprobados"
    
def bajoRiesgo():
    with open("modulo/storage/camper.json") as f:
        listaCamper =json.loads(f.read())
        f.close()
    with open("modulo/storage/notas.json") as f:
        data = json.loads(f.read())
        f.close()
        for datos in data:
            if ((int(datos["Teorica"])*0.3)+(int(datos["Practica"]))*0.6)+(int(datos["Trabajos"])*0.1) < 60:
                noAprobados = datos
                id=noAprobados["Id"]
                #print(aprobados)
                for camper in listaCamper:
                    if id==camper["Id"]:
                        print(f"""
Id: {camper.get('Id')}
Nombre: {camper.get('Nombre')}
Apellido: {camper.get('Apellido')}
Teorica: {noAprobados.get('Teorica')}
Practica: {noAprobados.get('Practica')}
Trabajos: {noAprobados.get('Trabajos')}
                              """)
    return "Lista de no aprobados"