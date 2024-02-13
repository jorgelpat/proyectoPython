import json
from os import system
import modulo.menu as menu
from .data import camper, estados


def guardar():
    system("clear")
    infoCamp = {
        "Nombre": "",
        "Apellido": "",
        "Edad": "",
        "Id": "",
        "Direccion": "",
        "Acudiente": "",
        "Telefono": "",
        "Estado": "",
        "Riesgo": "",
        "Warning": 0
    }
    infoCamp["Nombre"] = input("Ingrese nombre(s) del camper\n")
    infoCamp["Apellido"] = input("Ingrese apellido(s) del camper\n")
    bandera = True
    while (bandera):
        edad = input("Ingrese edad\n")
        if edad.isnumeric():
            infoCamp["Edad"]=edad
            bandera = False
        else:
            print("Dato no Valido")
    bandera = True
    while (bandera):
        id = input("Ingrese numero de identificacion\n")
        if id.isnumeric():
            infoCamp["Id"]=id
            bandera = False
        else:
            print("Dato no Valido")
    infoCamp["Direccion"] = input("Indique direccion de residencia\n")
    if int(infoCamp["Edad"])<18:
        infoCamp["Acudiente"] = input("Indique nombre completo del acudiente\n")
    else:
        infoCamp["Acudiente"] = None
    bandera = True
    while (bandera):
        tel = input("Indique numero de contacto\n")
        if tel.isnumeric():
            infoCamp["Telefono"]=tel
            bandera = False
        else:
             print("Dato no Valido")
    infoCamp["Estado"]="Preseleccion"
    # variable = input("Elija estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n" for i in estados]))
    # if variable=="1":
    #     infoCamp["Estado"]="Preseleccion"
    # elif variable=="2":
    #     infoCamp["Estado"]="Inscrito"
    # elif variable=="3":
    #     infoCamp["Estado"]="Aprobado"
    infoCamp["Riesgo"]="Normal"

    with open("modulo/storage/camper.json") as f:
        camper = json.load(f)
        
    camper.append(infoCamp)
    with open("modulo/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
        system("clear")
    return "Guardado Exitoso"


def actualizar():
    bandera=True
    while(bandera):
        system("clear")
        id = input("Ingrese identificacion del camper\n")
        with open("modulo/storage/camper.json", "r") as f:
            data = json.loads(f.read())
            for datos in data:
                if id==datos["Id"]:
                    datos["Nombre"]=input("Indique nombre del camper\n")
                    datos["Apellido"]=input("Indique apellido del camper\n")
                    bandera1=True
                    while(bandera1):
                        edad = input("Ingrese edad\n")
                        if edad.isnumeric():
                            datos["Edad"]=edad
                            bandera1 = False
                        else:
                            print("Dato no Valido")
                    bandera1 = True
                    while (bandera1):
                        id = input("Ingrese numero de identificacion\n")
                        if id.isnumeric():
                            datos["Id"]=id
                            bandera1 = False
                        else:
                            print("Dato no Valido")
                    datos["Direccion"] = input("Indique direccion de residencia\n")
                    if int(datos["Edad"])<18:
                        datos["Acudiente"] = input("Indique nombre completo del acudiente\n")
                    else:
                        datos["Acudiente"] = None
                    bandera1 = True
                    while (bandera1):
                        tel = input("Indique numero de contacto\n")
                        if tel.isnumeric():
                            datos["Telefono"]=tel
                            bandera1 = False
                        else:
                            print("Dato no Valido")
                    opt = input("Elija estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n" for i in estados]))
                    print(opt)
                    if opt == "1":
                        datos["Estado"] = "Preseleccion"
                    elif opt == "2":
                        datos["Estado"] = "Inscrito"
        bandera=False
    with open("modulo/storage/camper.json","w") as f:
        data = json.dumps(data, indent=4)
        f.write(data)
        f.close()



def actualizarEstado():
    bandera=True
    while(bandera):
        id = input("Identificacion del camper:\n")
        if id.isnumeric():
            bandera=False
    with open("modulo/storage/camper.json") as f:
        campers=json.loads(f.read())
        for camper in campers:
            if camper["Id"]==id:
                camper["Estado"]="Inscrito"
    with open("modulo/storage/camper.json","w") as f:
        campers=json.dumps(campers,indent=4)
        f.write(campers)
        f.close()
    while True:
        print(f"{camper.get("Nombre")} {camper.get("Apellido")} ha pasado a inscrito\n")
        print("Presione cualquier tecla seguido de 'ENTER' para salir\n")
        opc=input()
        if opc.isnumeric():
            break
        else:
            break
    system("clear")



def buscar():
    system("clear")
    while (True):
        id = input("Ingrese numero de identificacion del camper:\n")
        if id.isnumeric():
            break
    with open("modulo/storage/camper.json") as f:
        data=json.loads(f.read())
        f.close()
    for datos in data:
        if id == datos["Id"]:
            print(f"""
    Nombre: {datos.get('Nombre')}      
    Apellido: {datos.get('Apellido')}
    Edad: {datos.get('Edad')}
    Id: {datos.get('Id')}
    Direccion: {datos.get('Direccion')}
    Acudiente: {datos.get('Acudiente')}
    Teléfono: {datos.get('Telefono')}
    Estado: {datos.get('Estado')}                          
                """)
    bandera=True
    while(bandera):
        print("\t1. Seguir Buscando")
        print("\t2. Salir")
        opc=input()
        if opc.isnumeric():
            if opc == "1":
                buscar()
            elif opc =="2":
                bandera=False
                system("clear")
            else:
                system("clear")
    return "Camper cargado"

def eliminar():
    bandera=True
    while(bandera):
        id = input("Identificacion del camper a eliminar:\n")
        if id.isnumeric():
            bandera=False
    with open("modulo/storage/camper.json") as f:
        campers=json.loads(f.read())
        for camper in campers:
            if id == camper["Id"]:
                camper["Nombre"]= "",
                camper["Apellido"]= "",
                camper["Edad"]= "",
                camper["Id"]= "",
                camper["Direccion"]= "",
                camper["Acudiente"]= "",
                camper["Telefono"]= "",
                camper["Estado"]= "",
                camper["Riesgo"]= ""
    with open("modulo/storage/camper.json","w") as f:
        campers=json.dumps(campers, indent=4)
        f.write(campers)
        f.close()
    return "Camper Eliminado"




def menu():
    menu.menuCamper()


def inscritos():
    print("******CAMPER INSCRITOS******")
    with open("modulo/storage/camper.json") as f:
        campers = json.loads(f.read())
        f.close()
        for camper in campers:
            if camper["Estado"]=="Inscrito":
                print(f"""
****************************
Nombre: {camper.get("Nombre")}
Apellido: {camper.get("Apellido")}
Id: {camper.get("Id")}    
****************************                  
                      """)
    return "Camper Cargado"
