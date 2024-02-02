import json
from os import system
from .data import camper


def guardar():
    system("clear")
    info = {
        "Nombre": input("Ingrese nombre(s) del camper\n"),
        "Apellido": input("Ingrese apelido(s) del camper\n"),
        "Identificacion": input("Ingrese numero de identificacion\n"),
        "Direccion": input("Indique direccion de residencia\n"),
        "Acudiente": input("Indique nombre completo del acudiente\n"),
        "Telefono": int(input("Indique numero de contacto\n")),
        "Estado": input("Indique el estado del camper\n")
    }
    camper.append(info)
    with open("modulo/storage/camper.json", "w") as f:
        data = json.dumps(camper, ident=4)
        f.write(data)
        f.close()
    return "Guardado Exitoso"