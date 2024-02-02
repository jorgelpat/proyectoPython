import json
from os import system
import modulo.camper as camper


def menu():
    print("Seguimiento Academico de Campers")
    print("\t1. Registro de camper")
    print("\t2. Registro de pruebas")
    print("\t3. Registro de areas de entrenamiento")
    print("\t4. Crear rutas de entrenamiento")

bandera = True
while (bandera):
    menu()
    opc = int(input())
    match(opc):
        case 1:
            camper.guardar()
