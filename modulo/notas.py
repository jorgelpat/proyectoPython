from os import system
import json
from .data import notas, camper

def guardar():
    system("clear")
    infoNota = {
        "Id":"",
        "Teorica":"",
        "Practica":"",
        "Trabajos":""
    }
    bandera=True
    while (bandera):
        id = input("Escriba el documento del camper:")
        if id.isnumeric():
            infoNota["Id"] = id
            bandera=False
        else:
            print("Dato no Valido")
        teorica = input("Prueba teorica: ")
        if teorica.isnumeric():
            infoNota["Teorica"]=teorica
            bandera = False
        else:
            print("Dato no Valido")
    bandera=True
    while (bandera):
        practica = input("Prueba practica: ")
        if practica.isnumeric():
            infoNota["Practica"]=practica
            bandera = False
        else:
            print("Dato no Valido")
    bandera=True
    while (bandera):
        trabajos = input("Quizes y trabajos: ")
        if trabajos.isnumeric():
            infoNota["Trabajos"]=trabajos
            bandera = False
        else:
            print("Dato no Valido")

    with open("modulo/storage/notas.json") as f:
        notas = json.load(f)

    notas.append(infoNota)
    with open("modulo/storage/notas.json", "w") as f:
        data=json.dumps(notas, indent=4)
        f.write(data)
        f.close()
        system("clear")
    return "Guardado Exitoso"


def buscar():
    id = int(input("Indique la identificacion del camper\n"))
    with open("modulo/storage/notas.json") as f:
        data = json.loads(f.read())
        for datos in data:
            if id==datos["Id"]:
                print(datos)
    return "Notas Cargadas"

# def actualizar():
#     id = int(input("Identificación del camper:\n"))
#     with open("modulo/storage/notas.json") as f:
