from os import system
import modulo.camper as mCamper
import modulo.validate as valid
import modulo.notas as mNotas



def menuCamper():
    
    while(True):

        print("\t1. Registro de camper")
        print("\t2. Buscar Camper")
        print("\t3. Actualizar Camper")
        print("\t4. Eliminar Camper")
        print("\t5. Atrás")

        opc = int(input())
        match(opc):
            case 1:
                mCamper.guardar()
            case 2: mCamper.buscar()
            case 3: mCamper.actualizar()
            case 4: mCamper.eliminar()
            case 5: break
            case _: valid.noValid(opc)