from os import system
import json
import modulo.validate as validate
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
                    if (int(teorica)*0.3)+(int(practica)*0.6)+(int(trabajos)*0.1)<60:
                        camper["Riesgo"]="En Riesgo"
                        camper["Warning"]=camper["Warning"]+1
                        if camper["Warning"]==2:
                            camper["Estado"]="Filtrado"
                    with open("modulo/storage/camper.json","w") as f:
                        campers=json.dumps(campers,indent=4)
                        f.write(campers)
                        f.close()
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
        id = input("Indique la identificacion del camper\n")
        if id.isnumeric():
            break
    with open("modulo/storage/notas.json","r") as f:
        data = json.loads(f.read())
        f.close()
        for datos in data:
            if id==datos["Id"]:
                #print(datos)
                with open("modulo/storage/camper.json","r") as f1:
                    data1 = json.loads(f1.read())
                    f1.close()
                    for datos1 in data1:
                        if id==datos1["Id"]:
                            #print(datos1)
                            print(f"""
Modulo: {datos.get('Modulo')}
Nombre: {datos1.get('Nombre')}      
Apellido: {datos1.get('Apellido')}
Teorica: {datos.get('Teorica')}
Practica: {datos.get('Practica')}
Trabajos: {datos.get('Trabajos')}  
______________________________                 
                            """)
            else:
                print(f"No hay notas asociadadas a Id {id}")
    
        bandera=True
        while(bandera):
            print("\t1. Seguir Buscando")
            print("\t2. Salir")
            opc=input()
            if opc.isnumeric():
                if opc=="1":
                    system("clear")
                    buscar()
                elif opc=="2":
                    system("clear")
                    bandera=False
                else:
                    validate.noValid()
                
    return "Notas Cargadas"



def actNotas():
    system("clear")
    id = input("Documento de camper:\n")
    nModulo = input("Numero de módulo:\n")
    with open("modulo/storage/camper.json") as f1:
        campers=json.loads(f1.read())
    with open("modulo/storage/notas.json") as f:
        notas=json.loads(f.read())
        for nota in notas:
            if nota["Modulo"]==int(nModulo) and nota["Id"]==id:
                nota["Teorica"]=input("Teorica: ")
                nota["Practica"]=input("Practica: ")
                nota["Trabajos"]=input("Trabajos: ")
                with open ("modulo/storage/notas.json","w") as f:
                    notas=json.dumps(notas,indent=4)
                    f.write(notas)
                    f.close()#agregar funcionalidad adicional
                for camper in campers:
                    if id==camper["Id"]:
                        system("clear")
                        print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
                        print(f"""
Modulo: {nota.get('Modulo')}
Id: {nota.get('Id')}
Teorica: {nota.get('Teorica')}
Practica: {nota.get('Practica')}
Trabajos: {nota.get('Trabajos')}
                              """)
            else:
                print(f"No hay ninguna nota asociada al modulo {nModulo} con el Id {id}")

    bandera=True
    while (bandera):
        print("\t1. Seguir Buscando:")     
        print("\t2. Salir")
        opc=input()
        if opc.isnumeric():
            if opc=="1":
                system("clear")
                actNotas()
                bandera=False
            elif opc=="2":
                system("clear")
                break



def aprobados():
    with open("modulo/storage/camper.json") as f:
        campers=json.loads(f.read())
        for camper in campers:
            if camper["Estado"]=="Aprobado":
                system("clear")
                print(f"""{camper.get('Id')} {camper.get('Nombre')} {camper.get('Apellido')}""")
    while True:
        salir= input("\nPresiona 'Enter' para Salir")
        break
#     with open("modulo/storage/camper.json") as f:
#         listaCamper =json.loads(f.read())
#         f.close()
#     with open("modulo/storage/notas.json") as f:
#         data = json.loads(f.read())
#         f.close()
#         for datos in data:
#             if ((int(datos["Teorica"])*0.3)+(int(datos["Practica"]))*0.6)+(int(datos["Trabajos"])*0.1) >= 60:
#                 aprobados = datos
#                 id=aprobados["Id"]
#                 #print(aprobados)
#                 for camper in listaCamper:
#                     if id==camper["Id"]:
#                         print(f"""
# Id: {camper.get('Id')}
# Nombre: {camper.get('Nombre')}
# Apellido: {camper.get('Apellido')}
# Teorica: {aprobados.get('Teorica')}
# Practica: {aprobados.get('Practica')}
# Trabajos: {aprobados.get('Trabajos')}
#                               """)
#     while True:
#         print("\t1. Seguir Buscando:")     
#         print("\t2. Salir")
#         opc=input()
#         if opc.isnumeric():
#             if opc=="1":
#                 system("clear")
#                 actNotas()
#             elif opc=="2":
#                 system("clear")
#                 break
    return "Lista de aprobados"
    
def bajoRiesgo():
    with open("modulo/storage/camper.json") as f:
        campers=json.loads(f.read())
        for camper in campers:
            if camper["Riesgo"]=="En Riesgo":
                system("clear")
                print(f"""{camper.get('Id')} {camper.get('Nombre')} {camper.get('Apellido')}""")
    while True:
        salir= input("\nPresiona 'Enter' para Salir")
        break
#     with open("modulo/storage/camper.json") as f:
#         listaCamper =json.loads(f.read())
#         f.close()
#     with open("modulo/storage/notas.json") as f:
#         data = json.loads(f.read())
#         f.close()
#         for datos in data:
#             if ((int(datos["Teorica"])*0.3)+(int(datos["Practica"]))*0.6)+(int(datos["Trabajos"])*0.1) < 60:
#                 noAprobados = datos
#                 id=noAprobados["Id"]
#                 #print(aprobados)
#                 for camper in listaCamper:
#                     if id==camper["Id"]:
#                         print(f"""
# Id: {camper.get('Id')}
# Nombre: {camper.get('Nombre')}
# Apellido: {camper.get('Apellido')}
# Teorica: {noAprobados.get('Teorica')}
# Practica: {noAprobados.get('Practica')}
# Trabajos: {noAprobados.get('Trabajos')}
#                               """)
    return "Lista de no aprobados"


def lista_aprob_camper_trainer_modulo():
    with open("modulo/storage/horario1.json") as f1:
        horario1=json.loads(f1.read())
    with open("modulo/storage/horario2.json") as f2:
        horario2=json.loads(f2.read())
    with open("modulo/storage/horario3.json") as f3:
        horario3=json.loads(f3.read())
    with open("modulo/storage/horario4.json") as f4:
        horario4=json.loads(f4.read())
    with open("modulo/storage/notas.json") as f:
        notas=json.loads(f.read())
        contador=0
        for nota in notas:
            if ((int(nota["Practica"])*0.6)+(int(nota["Teorica"])*0.3)+((int(nota["Trabajos"]))*0.1))>=60:
                contador = contador+1
                for datos1 in horario1:
                    if nota["Id"]==datos1["Campers"]:
                        print(f"Trainer: ........{datos1.get('Trainer')}")
                        print(f"Camper: .........{nota.get('Id')}")
                for datos2 in horario2:
                    if nota["Id"]==datos2["Campers"]:
                        print(f"Trainer: ........{datos2.get('Trainer')}")
                        print(f"Camper: .........{nota.get('Id')}")
                for datos3 in horario3:
                    if nota["Id"]==datos3["Campers"]:
                        print(f"Trainer: ........{datos3.get('Trainer')}")
                        print(f"Camper: .........{nota.get('Id')}")
                for datos4 in horario4:
                    if nota["Id"]==datos4["Campers"]:
                        print(f"Trainer: ........{datos4.get('Trainer')}")
                        print(f"Camper: .........{nota.get('Id')}")
    print("Lista de numero de examenes aprobados y reprobados")
    print(f"Cantidad de examenes aprobados: {contador}")

    input("Presione 'Enter' para salir")
    



    # with open("modulo/storage/camper.json") as f:
    #     campers=json.loads(f.read())
    # with open("modulo/storage/horario1.json") as f1:
    #     horario1=json.loads(f1.read())
    # with open("modulo/storage/horario2.json") as f2:
    #     horario2=json.loads(f2.read())
    # with open("modulo/storage/horario3.json") as f3:
    #     horario3=json.loads(f3.read())
    # with open("modulo/storage/horario4.json") as f4:
    #     horario4=json.loads(f4.read())
    # with open("modulo/storage/notas.json") as f5:
    #     notas=json.loads(f5.read())