from os import system
import modulo.camper as mCamper
import modulo.validate as valid
import modulo.notas as mNotas



def menuCamper():
    system("clear")
    while(True):

        print("\t1. Registro de camper")
        print("\t2. Buscar Camper")
        print("\t3. Actualizar Camper")
        print("\t4. Eliminar Camper")
        print("\t5. Atrás")

        opc = input()
        match(opc):
            case "1":
                mCamper.guardar()
            case "2": mCamper.buscar()
            case "3":
                system("clear")
                bandera=True
                while(bandera): 
                    print("\t1. Actualizar Informacion completa del Camper")
                    print("\t2. Actualizar Estado a Inscrito")
                    opc=input()
                    if opc.isnumeric():
                        bandera=False
                    if opc=="1":
                        mCamper.actualizar()
                    elif opc=="2":
                        mCamper.actualizarEstado()
                    else:
                        valid.noValid()
            case "4": mCamper.eliminar()
            case "5": break
            case _: valid.noValid(opc)