from os import system

def guardar():
    system("clear")
    info = {
        "Nombre": input("Ingrese nombre(s) del camper"),
        "Apellido": input("Ingrese apelido(s) del camper"),
        "Identificacion": input("Ingrese numero de identificacion"),
        "Direccion": input("Indique direccion de residencia"),
        "Acudiente": input("Indique nombre completo del acudiente"),
        "Telefono": int("Indique numero de contacto"),
        "Estado": input("Estado del camper")
    }