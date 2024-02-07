import json
from os import system
import modulo.menu as menu
from .data import camper, estados, trainer

def guardar():
    infoTrainer = {
        "Nombre": "",
        "Apellido": "",
        "Id": ""
    }
    infoTrainer["Nombre"]=input("Nombre del trainer:\n")
    infoTrainer["Apellido"]=input("Apellido del trainer:\n")
    bandera=True
    while (bandera):
        id=input("Id:\n")
        if id.isnumeric():
            infoTrainer["Id"]=id
            bandera = False
    with open("modulo/storage/trainer.json") as f:
        trainer=json.loads(f.read())
        f.close()
        trainer.append(infoTrainer)
    with open("modulo/storage/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Guardado Exitoso"






def menuTrainer():
    print("\t1. Crear trainer")
    opc = int(input())
    if opc==1:
        guardar()

