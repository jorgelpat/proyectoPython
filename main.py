import json
from os import system
import modulo.camper as mCamper
import modulo.notas as mNotas
import modulo.validate as valid


def menuCamper():
    print("\t1. Registro de camper")
    print("\t2. Buscar Camper")
    print("\t3. Actualizar Camper")
    print("\t4. Eliminar Camper")

    bandera1 = True
    while (bandera1):
        opc = int(input())
        match(opc):
            case 1:
                mCamper.guardar()
                bandera1 = False
            case 2: mCamper.buscar()
            case 3: mCamper.actualizar()
            case 4: mCamper.eliminar()
            case _: valid.noValid(opc)
        


def menu():
    print("Seguimiento Academico de Campers")
    print("\t1. Modulo camper")
    print("\t2. Registro de pruebas")
    print("\t3. Registro de areas de entrenamiento")
    print("\t4. Crear rutas de entrenamiento")

bandera = True
while (bandera):
    menu()
    opc = int(input())
    match(opc):
        case 1:
            menuCamper()
        case 2:
            mNotas.guardar()

