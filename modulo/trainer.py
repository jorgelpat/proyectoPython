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

def actualizar():
    id = input("Ingrese Id:\n")
    with open("modulo/storage/trainer.json") as f:
        listTrainer = json.loads(f.read())
        f.close()
        for trainer in listTrainer:
            if id==trainer["Id"]:
                trainer["Nombre"]=input("Nombre del trainer:\n")
                trainer["Apellido"]=input("Apellido del trainer:\n")
                bandera=True
                while(bandera):
                    newId=input("Id del trainer:\n")
                    if newId.isnumeric():
                        trainer["Id"]=newId
                        bandera=False
    with open("modulo/storage/trainer.json","w") as f:
        listTrainer = json.dumps(listTrainer, indent=4)
        f.write(listTrainer)
        f.close()
    return "Edicion Terminada"

def buscar():
    bandera=True
    while(bandera):
        id = input("Id del trainer:\n")
        if id.isnumeric():
            bandera=False
    with open("modulo/storage/trainer.json") as f:
        trainers = json.loads(f.read())
        f.close()
        for trainer in trainers:
            if id==trainer["Id"]:
                print(f"""
Nombre: {trainer.get("Nombre")}
Apellido: {trainer.get("Apellido")}
Id: {trainer.get("Id")}  
                      """)
    return "Trainer Cargado"

        
            
        






def menuTrainer():
    print("\t1. Crear trainer")
    print("\t2. Editar trainer")
    print("\t3. Buscar trainer")
    opc = int(input())
    if opc==1:
        guardar()
    elif opc==2:
        actualizar()
    elif opc==3:
        buscar()


