import json
from os import system
import modulo.camper as mCamper
import modulo.notas as mNotas
import modulo.validate as valid
import modulo.menu as menus


bandera = True
while (bandera):
    menus.menuPrincipal()
    opc = int(input())
    match(opc):
        case 1:
            menus.menuCamper()
        case 2:
            mNotas.guardar()

