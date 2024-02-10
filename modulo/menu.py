from os import system
import modulo.camper as mCamper
import modulo.validate as valid
import modulo.notas as mNotas



def menuCamper():
    bandera1 = True
    print("\t1. Registro de camper")
    print("\t2. Buscar Camper")
    print("\t3. Actualizar Camper")
    print("\t4. Eliminar Camper")
    print("\t5. Atrás")

    while (bandera1):
        opc = int(input())
        match(opc):
            case 1:
                mCamper.guardar()
                bandera1 = False
            case 2: mCamper.buscar()
            case 3: mCamper.actualizar()
            case 4: mCamper.eliminar()
            case 5: bandera1=False
            case _: valid.noValid(opc)