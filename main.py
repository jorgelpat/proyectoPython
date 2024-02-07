import json
from os import system
import modulo.camper as mCamper
import modulo.trainer as mTrainer
import modulo.notas as mNotas
import modulo.validate as valid
import modulo.menu as menu

def menuPrincipal():
    #system("clear")
    print("Seguimiento Academico de Campers")
    print("\t1. Modulo camper")
    print("\t2. Modulo notas")
    print("\t3. Modulo trainer")
    print("\t4. Crear rutas de entrenamiento")
    print("\t5. Ver informacion Camper")
    print("\t6. Listas de Campers")
    opc = int(input())
    match(opc):
        case 1: menu.menuCamper()
        case 2: 
            #system("clear")
            print("\t1. Ver notas")
            print("\t2. Registrar notas")
            print("\t3. Actualizar notas")
            print("\t4. Atrás")
            opc = int(input())
            match(opc):
                case 1: mNotas.buscar()
                case 2: mNotas.guardar()
                case 4: menuPrincipal()
        case 3: mTrainer.menuTrainer()
        case 6:
            print("\t1. Campers Aprobados")
            print("\t2. Campers con bajo rendimiento")
            print("\t3. Lista de Inscritos")
            print("\t4. Lista de Trainers")
            opc= int(input())
            match(opc):
                case 1:
                    mNotas.aprobados()
                case 2:
                    mNotas.bajoRiesgo()
                case 3:
                    mCamper.inscritos()
                case 4:
                    mTrainer.listaTrainers()


bandera = True
while (bandera):
    menuPrincipal()
    

