from os import system

def guardar():
    system("clear")
    infoNota = {
        "Teorica":"",
        "Practica":"",
        "Trabajos":""
    }
    bandera=True
    while (bandera):
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

