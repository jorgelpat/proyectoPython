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
            if (int(datos["Teorica"])+int(datos["Practica"]))/2 >= 60:
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
    
            