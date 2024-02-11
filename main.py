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
    system("clear")
    bandera=True
    while(bandera):
        print("Seguimiento Academico de Campers")
        print("\t1. Menu Camper")
        print("\t2. Menu notas")
        print("\t3. Menu trainer")
        print("\t4. Probar notas trainer")#No se usa
        print("\t5. Asiganacion Horaria")
        print("\t6. Listas de Campers")
        print("\t7. Rutas")

        opc = input()
        if opc.isnumeric():
            bandera=False
    match(opc):
        case "1": menu.menuCamper()
        case "2": 
            system("clear")
            bandera=True
            while(bandera):
                print("*****Menu Notas*****")
                print("\t1. Ver notas")
                print("\t2. Registrar notas")
                print("\t3. Actualizar notas")
                print("\t4. Atrás")
                opc = input()
                if opc.isnumeric():
                    bendera=False
            match(opc):
                case "1": mNotas.buscar()
                case "2": mNotas.guardarNotasModulo()#Falta opcion 3
                case "4": menuPrincipal()
        case "3": mTrainer.menuTrainer()
        case "5":
            system("clear")
            bandera=True
            while(bandera):
                print("********Asignacion de Horarios********")
                print("\t1. Asiganacion Horaria de Trainers")
                print("\t2. Asignacion Horaria de Campers")
                opc = input()
                if opc.isnumeric():
                    bandera=False
            if opc == "1":
                system("clear")
                bandera=True
                while(bandera):
                    print("***Horas Disponibles***")
                    print("\t1. 06am a 10am")
                    print("\t2. 10am a 02pm")
                    print("\t3. 02pm a 06pm")
                    print("\t4. 06pm a 10pm")
                    opc=input()
                    if opc.isnumeric():
                        bandera=False
                if opc == "1":
                    system("clear")
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_trainer_hora1_area1()
                    elif opc == "2":
                        mHorarios.ingreso_trainer_hora1_area2()
                    elif opc == "3":
                        mHorarios.ingreso_trainer_hora1_area3()
                    elif opc == "0":
                        menuPrincipal()
                if opc == "2":
                    system("clear")
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_trainer_hora2_area1()
                    elif opc == "2":
                        mHorarios.ingreso_trainer_hora2_area2()
                    elif opc == "3":
                        mHorarios.ingreso_trainer_hora2_area3()
                    elif opc == "0":
                        menuPrincipal()
                if opc == "3":
                    system("clear")
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_trainer_hora3_area1()
                    elif opc == "2":
                        mHorarios.ingreso_trainer_hora3_area2()
                    elif opc == "3":
                        mHorarios.ingreso_trainer_hora3_area3()
                    elif opc == "0":
                        menuPrincipal()
                if opc == "4":
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_trainer_hora4_area1()
                    elif opc == "2":
                        mHorarios.ingreso_trainer_hora4_area2()
                    elif opc == "3":
                        mHorarios.ingreso_trainer_hora4_area3()
                    elif opc == "0":
                        menuPrincipal()
            if opc == "2":
                system("clear")
                bandera=True
                while(bandera):
                    print("***Horas Disponibles***")
                    print("\t1. 06am a 10am")
                    print("\t2. 10am a 02pm")
                    print("\t3. 02pm a 06pm")
                    print("\t4. 06pm a 10pm")
                    opc=input()
                    if opc.isnumeric():
                        bandera=False
                if opc == "1":
                    system("clear")
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandea=False
                    if opc == "1":
                        mHorarios.ingreso_camper_hora1_area1()
                    elif opc == "2":
                        mHorarios.ingreso_camper_hora1_area2()
                    elif opc == "3":
                        mHorarios.ingreso_camper_hora1_area3()
                    elif opc == "0":
                        menuPrincipal()
                if opc == "2":
                    system("clear")
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_camper_hora2_area1()
                    elif opc == "2":
                        mHorarios.ingreso_camper_hora2_area2()
                    elif opc == "3":
                        mHorarios.ingreso_camper_hora2_area3()
                    elif opc == "0":
                        menuPrincipal()
                if opc == "3":
                    system("clear")
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_camper_hora3_area1()
                    elif opc == "2":
                        mHorarios.ingreso_camper_hora3_area2()
                    elif opc == "3":
                        mHorarios.ingreso_camper_hora3_area3()
                    elif opc == "0":
                        menuPrincipal()
                if opc == "4":
                    bandera=True
                    while(bandera):
                        print("Ruta de entrenamiento")
                        print("\t1. Netcore")
                        print("\t2. NodeJS")
                        print("\t3. Java")
                        print("\t0. ******Salir******")
                        opc = input()
                        if opc.isnumeric():
                            bandera=False
                    if opc == "1":
                        mHorarios.ingreso_camper_hora4_area1()
                    elif opc == "2":
                        mHorarios.ingreso_camper_hora4_area2()
                    elif opc == "3":
                        mHorarios.ingreso_camper_hora4_area3()
                    elif opc == "0":
                        menuPrincipal()
        case "6":
            system("clear")
            bandera=True
            while(bandera):
                print("\t1. Campers Aprobados")
                print("\t2. Campers con bajo rendimiento")
                print("\t3. Lista de Inscritos")
                print("\t4. Lista de Trainers")
                opc= input()
                if opc.isnumeric():
                    bandera=False
            match(opc):
                case "1":
                    mNotas.aprobados()
                case "2":
                    mNotas.bajoRiesgo()
                case "3":
                    mCamper.inscritos()
                case "4":
                    mTrainer.listaTrainers()
                    
        case "7": mRuta.enrutamiento()


bandera=True
while (bandera):
    menuPrincipal()





