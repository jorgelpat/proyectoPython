from os import system

def guardar():
    system("clear")
    info = {
        "Nombre": input("Ingrese nombre(s) del camper\n"),
        "Apellido": input("Ingrese apelido(s) del camper\n"),
        "Identificacion": input("Ingrese numero de identificacion\n"),
        "Direccion": input("Indique direccion de residencia\n"),
        "Acudiente": input("Indique nombre completo del acudiente\n"),
        "Telefono": int("Indique numero de contacto\n"),
        "Estado": input("Indique el estado del camper\n")
    }