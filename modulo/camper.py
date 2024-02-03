import json
from os import system
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
        "Estado": ""
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
    infoCamp["Estado"] = input("Elija estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n"for i in estados]))
    camper.append(infoCamp)
    # with open("modulo/storage/camper.json", "w") as f:
    #     data = json.dumps(camper, ident=4)
    #     f.write(data)
    #     f.close()
    # return "Guardado Exitoso"