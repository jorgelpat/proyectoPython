import json
from os import system
import modulo.menu as menu
from .data import camper, estados


def guardar():
    #system("clear")
    infoCamp = {
        "Nombre": "",
        "Apellido": "",
        "Edad": "",
        "Id": "",
        "Direccion": "",
        "Acudiente": "",
        "Telefono": "",
        "Estado": "Preinscrito",

    }
    infoCamp["Nombre"] = input("Ingrese nombre(s) del camper\n")
    infoCamp["Apellido"] = input("Ingrese apellido(s) del camper\n")
    bandera = True
    while (bandera):
        edad = input("Ingrese edad\n")
        if edad.isnumeric():
            infoCamp["Edad"]=edad
            bandera = False
        else:
            print("Dato no Valido")
    bandera = True
    while (bandera):
        id = input("Ingrese numero de identificacion\n")
        if id.isnumeric():
            infoCamp["Id"]=id
            bandera = False
        else:
            print("Dato no Valido")
    infoCamp["Direccion"] = input("Indique direccion de residencia\n")
    if int(infoCamp["Edad"])<18:
        infoCamp["Acudiente"] = input("Indique nombre completo del acudiente\n")
    else:
        infoCamp["Acudiente"] = None
    bandera = True
    while (bandera):
        tel = input("Indique numero de contacto\n")
        if tel.isnumeric():
            infoCamp["Telefono"]=tel
            bandera = False
        else:
             print("Dato no Valido")
    #infoCamp["Estado"] = input("Elija estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n" for i in estados]))

    with open("modulo/storage/camper.json") as f:
        camper = json.load(f)
        
    camper.append(infoCamp)
    with open("modulo/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
        #system("clear")
    return "Guardado Exitoso"


def actualizar():
    bandera=True
    while(bandera):
        system("clear")
        id = input("Ingrese identificacion del camper\n")
        with open("modulo/storage/camper.json", "r") as f:
            data = json.loads(f.read())
            for datos in data:
                if id==datos["Id"]:
                    datos["Nombre"]=input("Indique nombre del camper\n")
                    datos["Apellido"]=input("Indique apellido del camper\n")
                    bandera1=True
                    while(bandera1):
                        edad = input("Ingrese edad\n")
                        if edad.isnumeric():
                            datos["Edad"]=edad
                            bandera1 = False
                        else:
                            print("Dato no Valido")
                    bandera1 = True
                    while (bandera1):
                        id = input("Ingrese numero de identificacion\n")
                        if id.isnumeric():
                            datos["Id"]=id
                            bandera1 = False
                        else:
                            print("Dato no Valido")
                    datos["Direccion"] = input("Indique direccion de residencia\n")
                    if int(datos["Edad"])<18:
                        datos["Acudiente"] = input("Indique nombre completo del acudiente\n")
                    else:
                        datos["Acudiente"] = None
                    bandera1 = True
                    while (bandera1):
                        tel = input("Indique numero de contacto\n")
                        if tel.isnumeric():
                            datos["Telefono"]=tel
                            bandera1 = False
                        else:
                            print("Dato no Valido")
                    datos["Estado"] = input("Elija estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n" for i in estados]))
                else:
                    print("no hay ningun camper registrado con esa identificacion")
        with open("modulo/storage/camper.json","w") as f:
            data = json.dumps(data, indent=4)
            f.write(data)
            f.close()            
        print("Operacion Terminada")
        print("\t1. Salir")
        print("\t2. Seguir editando")

    return "Edicion Terminada" #No terminado, Error en la salida, no da opcion de salir




            
#         print(f"""
# Codigo: {code}
# Nombre: {camper[code].get('Nombre')}
# Apellido: {camper[code].get('Apellido')}
# Edad: {camper[code].get('Edad')}
# Id: {camper[code].get('Id')}
# Direccion: {camper[code].get('Direccion')}
# Acudiente: {camper[code].get('Acudiente')}
# Telefono: {camper[code].get('Telefono')}
#               """)
        # print("¿Este es el camper que deseas actualizar?")
        # print("1. Sí")
        # print("2. No")
        # print("3. Salir")
        # bandera=True
        # while(bandera):
        #     opc = int(input())
        #     if opc == 1:
        #         system("clear")
        #         infoCamp = {
        #         "Nombre": "",
        #         "Apellido": "",
        #         "Edad": "",
        #         "Id": "",
        #         "Direccion": "",
        #         "Acudiente": "",
        #         "Telefono": "",
        #         "Estado": ""
        #         }
        #         infoCamp["Nombre"] = input("Ingrese nombre(s) del camper\n")
        #         infoCamp["Apellido"] = input("Ingrese apellido(s) del camper\n")
        #         bandera = True
        #         while (bandera):
        #             edad = input("Ingrese edad\n")
        #             if edad.isnumeric():
        #                 infoCamp["Edad"]=edad
        #                 bandera = False
        #             else:
        #                 print("Dato no Valido")
        #         bandera = True
        #         while (bandera):
        #             id = input("Ingrese numero de identificacion\n")
        #             if id.isnumeric():
        #                 infoCamp["Id"]=id
        #                 bandera = False
        #             else:
        #                 print("Dato no Valido")
        #         infoCamp["Direccion"] = input("Indique direccion de residencia\n")
        #         if int(infoCamp["Edad"])<18:
        #             infoCamp["Acudiente"] = input("Indique nombre completo del acudiente\n")
        #         else:
        #             infoCamp["Acudiente"] = None
        #         bandera = True
        #         while (bandera):
        #             tel = input("Indique numero de contacto\n")
        #             if tel.isnumeric():
        #                 infoCamp["Telefono"]=tel
        #                 bandera = False
        #             else:
        #                 print("Dato no Valido")
        #         infoCamp["Estado"] = input("Elija estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n"for i in estados]))
        #         camper[code]=infoCamp
        #         with open("modulo/storage/camper.json","w") as f:
        #             data = json.dumps(camper, indent=4)
        #             f.write(data)
        #             f.close()
        #     if opc == 2:
        #         actualizar()
        #     if opc == 3:
        #         bandera = False
        # return "Edicion Terminada"


def buscar():
    bandera = True
    while (bandera):
        system("clear")
    #     for i, val in enumerate(camper):
    #         print(f"""
    # Código: {i}
    # Nombre: {val.get('Nombre')}      
    # Apellido: {val.get('Apellido')}
    # Edad: {val.get('Edad')}
    # Id: {val.get('Id')}
    # Direccion: {val.get('Direccion')}
    # Acudiente: {val.get('Acudiente')}
    # Teléfono: {val.get('Telefono')}
    # Estado: {val.get('Estado')}
    #               """)
        id = input("Ingrese numero de identificacion del camper:\n")
        with open("modulo/storage/camper.json") as f:
            data=json.loads(f.read())
            f.close()
            for datos in data:
                if id == datos["Id"]:
                    print(f"""
    Nombre: {datos.get('Nombre')}      
    Apellido: {datos.get('Apellido')}
    Edad: {datos.get('Edad')}
    Id: {datos.get('Id')}
    Direccion: {datos.get('Direccion')}
    Acudiente: {datos.get('Acudiente')}
    Teléfono: {datos.get('Telefono')}
    Estado: {datos.get('Estado')}                          
                        """)
        print("\t1. Salir\n")
        opc = int(input())
        if opc == 1:
            menu()
            #No es posible salir de la funcion
            #Error al cargar la funcion

    return "Camper cargado"



# def eliminar():
    # bandera=True
    # while (bandera):
    #     system("clear")
    #     id = int(input("Ingrese identidad del camper\n"))
    #     with open("modulo/storage/camper.json") as f:
    #         data=json.loads(f)
    #         data["Nombre"]:

#         print(f"""
# codigo: {code}
# Nombre: {camper[code].get('Nombre')}              
# Apellido: {camper[code].get('Apellido')}
# Edad: {camper[code].get('Edad')}
# Id: {camper[code].get('Id')}
# Direccion: {camper[code].get('Direccion')}
# Acudiente: {camper[code].get('Acudiente')}
# Telefono: {camper[code].get('Telefono')}              
#               """)
        # print("¿Este es el camper que deseas eliminar?")
        # print("1. Si")
        # print("2. No")
        # print("3. Salir")
        # opc = int(input())
        # if opc==1:
        #     camper.pop(code)
        #     with open("modulo/storage/camper.json", "w") as f:
        #         data = json.dumps(camper,indent=4)
        #         f.write(code)
        #         f.close()
        #     bandera = False
        # if opc==2:
        #     eliminar()
        # if opc==3:
        #     bandera = False

def menu():
    menu.menuCamper()
    # system("clear")
    # print("Menu Camper")
    # print("\t1. Registro de camper")
    # print("\t2. Buscar Camper")
    # print("\t3. Actualizar Camper")
    # print("\t4. Eliminar Camper")
    # print("\t5. Salir")

    
    # bandera = True
    # while (bandera):
    #     opc = int(input())
    #     match(opc):
    #         case 1:
    #             guardar()
    #         case 2:
    #             buscar()
    #         case 3:
    #             actualizar()
    #         # case 4:
    #         #     eliminar()

def inscritos():
    print("******CAMPER INSCRITOS******")
    with open("modulo/storage/camper.json") as f:
        campers = json.loads(f.read())
        f.close()
        for camper in campers:
            if camper["Estado"]=="2":
                print(f"""
****************************
Nombre: {camper.get("Nombre")}
Apellido: {camper.get("Apellido")}
Id: {camper.get("Id")}    
****************************                  
                      """)
    return "Camper Cargado"
