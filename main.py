import json
from os import system
import modulo.camper as mCamper
import modulo.trainer as mTrainer
import modulo.notas as mNotas
import modulo.validate as valid
import modulo.menu as menu
import modulo.rutas as mRuta
import modulo.horarios as mHorarios

def menuPrincipal():
    #system("clear")
    print("Seguimiento Academico de Campers")
    print("\t1. Modulo camper")
    print("\t2. Modulo notas")
    print("\t3. Modulo trainer")
    print("\t4. Probar notas trainer")
    print("\t5. prueba horarios trainer")
    print("\t6. Listas de Campers")
    print("\t7. Rutas")
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
                case 2: mNotas.guardarNotasModulo()#Falta opcion 3
                case 4: menuPrincipal()
        case 3: mTrainer.menuTrainer()
        case 4: mNotas.preNotas()
        case 5: mHorarios.ingreso_trainer_hora1()
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
                    
        case 7: mRuta.enrutamiento()


bandera = True
while (bandera):
    menuPrincipal()
    

