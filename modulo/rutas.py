import json
from .data import rutas

def enrutamiento():
    ruta= {
        "Id": "",
        "Ruta":""
    }
    bandera=True
    while (bandera):
        id = input("Indique numero de identificacion del camper:")
        if id.isnumeric():
            ruta["Id"]=id
            bandera=False
        else:
            "Documento no valido"
        bandera1=True
        while(bandera1):
            rut = input("Elija la ruta del camper \n\t"+"\t".join([f"{rutas.index(i)+1}. {i}\n"for i in rutas]))
            if rut==1:
                ruta["Ruta"]="NodeJS"
                bandera1==False#Arreglar estos pasos
            elif rut==2:
                ruta["Ruta"]="Java"
                bandera1==False
            elif rut==3:
                ruta["Ruta"]="Netcore"
                bandera1==False
        with open("modulo/storage/rutas.json") as f:
            rutas1 = json.loads(f.read())
            f.close()
            rutas1.append(ruta)
        with open("modulo/storage/rutas.json","w") as f:
            data=json.dumps(rutas1, indent=4)
            f.write(data)
            f.close()
            
def lista_ruta_netcore():
    with open("modulo/storage/trainer.json") as f:#Trainer
        trainers=json.loads(f.read())
    with open("modulo/storage/horario1.json") as f:#Horario1
        horario1=json.loads(f.read())
        #print("Trainers:")
        for data in horario1:
            if data["Ruta"]=="NetCore":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/camper.json") as f:#Camper
        campers=json.loads(f.read())
    with open("modulo/storage/horario1.json") as f:#Horario1
        horario1=json.loads(f.read())
        #print("Campers:")
        for datos in horario1:
            if datos["Ruta"]=="NetCore":
                for i in range(len(datos["Campers"])):
                    # print(f"""
                    #     Id:{datos.get('Campers')[i]}
                    #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    with open("modulo/storage/trainer.json") as f:#Trainer
        trainers=json.loads(f.read())
    with open("modulo/storage/horario2.json") as f:#Horario2
        horario2=json.loads(f.read())
        #print("Trainers:")
        for data in horario2:
            if data["Ruta"]=="NetCore":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario2.json") as f:
        horario2=json.loads(f.read())
        for datos in horario2:
            if datos["Ruta"]=="NetCore":
                for i in range(len(datos["Campers"])):
                    # print(f"""
                    #     Id:{datos.get('Campers')[i]}
                    #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
                
    with open("modulo/storage/horario3.json") as f:
        horario3=json.loads(f.read())
        #print("Trainer:")
        for data in horario3:
            if data["Ruta"]=="NetCore":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario3.json") as f:
        horario3=json.loads(f.read())
        for datos in horario3:
            if datos["Ruta"]=="NetCore":
                for i in range(len(datos["Campers"])):
            # print(f"""
            #     Id:{datos.get('Campers')[i]}
            #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    with open("modulo/storage/horario4.json") as f:
        horario4=json.loads(f.read())
        #print("Trainer:")
        for data in horario4:
            if data["Ruta"]=="NetCore":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario4.json") as f:
        horario4=json.loads(f.read())
        for datos in horario4:
            if datos["Ruta"]=="NetCore":
                for i in range(len(datos["Campers"])):
            # print(f"""
            #     Id:{datos.get('Campers')[i]}
            #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    bandera=True
    while(bandera):
        print("\t1. Salir")
        opc=input()
        if opc.isnumeric():
            bandera=False#Mejorar




def lista_ruta_nodejs():
    with open("modulo/storage/trainer.json") as f:#Trainer
        trainers=json.loads(f.read())
    with open("modulo/storage/horario1.json") as f:#Horario1
        horario1=json.loads(f.read())
        #print("Trainers:")
        for data in horario1:
            if data["Ruta"]=="NodeJS":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/camper.json") as f:#Camper
        campers=json.loads(f.read())
    with open("modulo/storage/horario1.json") as f:#Horario1
        horario1=json.loads(f.read())
        #print("Campers:")
        for datos in horario1:
            if datos["Ruta"]=="NodeJS":
                for i in range(len(datos["Campers"])):
                    # print(f"""
                    #     Id:{datos.get('Campers')[i]}
                    #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    with open("modulo/storage/trainer.json") as f:#Trainer
        trainers=json.loads(f.read())
    with open("modulo/storage/horario2.json") as f:#Horario2
        horario2=json.loads(f.read())
        #print("Trainers:")
        for data in horario2:
            if data["Ruta"]=="NodeJS":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario2.json") as f:
        horario2=json.loads(f.read())
        for datos in horario2:
            if datos["Ruta"]=="NodeJS":
                for i in range(len(datos["Campers"])):
                    # print(f"""
                    #     Id:{datos.get('Campers')[i]}
                    #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
                
    with open("modulo/storage/horario3.json") as f:
        horario3=json.loads(f.read())
        #print("Trainer:")
        for data in horario3:
            if data["Ruta"]=="NodeJS":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario3.json") as f:
        horario3=json.loads(f.read())
        for datos in horario3:
            if datos["Ruta"]=="NodeJS":
                for i in range(len(datos["Campers"])):
            # print(f"""
            #     Id:{datos.get('Campers')[i]}
            #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    with open("modulo/storage/horario4.json") as f:
        horario4=json.loads(f.read())
        #print("Trainer:")
        for data in horario4:
            if data["Ruta"]=="NodeJS":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario4.json") as f:
        horario4=json.loads(f.read())
        for datos in horario4:
            if datos["Ruta"]=="NodeJS":
                for i in range(len(datos["Campers"])):
            # print(f"""
            #     Id:{datos.get('Campers')[i]}
            #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    bandera=True
    while(bandera):
        print("\t1. Salir")
        opc=input()
        if opc.isnumeric():
            bandera=False#Mejorar




def lista_ruta_java():
    with open("modulo/storage/trainer.json") as f:#Trainer
        trainers=json.loads(f.read())
    with open("modulo/storage/horario1.json") as f:#Horario1
        horario1=json.loads(f.read())
        #print("Trainers:")
        for data in horario1:
            if data["Ruta"]=="Java":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/camper.json") as f:#Camper
        campers=json.loads(f.read())
    with open("modulo/storage/horario1.json") as f:#Horario1
        horario1=json.loads(f.read())
        #print("Campers:")
        for datos in horario1:
            if datos["Ruta"]=="Java":
                for i in range(len(datos["Campers"])):
                    # print(f"""
                    #     Id:{datos.get('Campers')[i]}
                    #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    with open("modulo/storage/trainer.json") as f:#Trainer
        trainers=json.loads(f.read())
    with open("modulo/storage/horario2.json") as f:#Horario2
        horario2=json.loads(f.read())
        #print("Trainers:")
        for data in horario2:
            if data["Ruta"]=="Java":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario2.json") as f:
        horario2=json.loads(f.read())
        for datos in horario2:
            if datos["Ruta"]=="Java":
                for i in range(len(datos["Campers"])):
                    # print(f"""
                    #     Id:{datos.get('Campers')[i]}
                    #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
                
    with open("modulo/storage/horario3.json") as f:
        horario3=json.loads(f.read())
        #print("Trainer:")
        for data in horario3:
            if data["Ruta"]=="Java":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario3.json") as f:
        horario3=json.loads(f.read())
        for datos in horario3:
            if datos["Ruta"]=="Java":
                for i in range(len(datos["Campers"])):
            # print(f"""
            #     Id:{datos.get('Campers')[i]}
            #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    with open("modulo/storage/horario4.json") as f:
        horario4=json.loads(f.read())
        #print("Trainer:")
        for data in horario4:
            if data["Ruta"]=="Java":
                for trainer in trainers:
                    if trainer["Id"]==data.get('Trainer'):
                        print(f"""
{trainer.get('Nombre')} {trainer.get('Apellido')}***
                              """)
    with open("modulo/storage/horario4.json") as f:
        horario4=json.loads(f.read())
        for datos in horario4:
            if datos["Ruta"]=="Java":
                for i in range(len(datos["Campers"])):
            # print(f"""
            #     Id:{datos.get('Campers')[i]}
            #     """)
                    for camper in campers:
                        if datos.get('Campers')[i]==camper["Id"]:
                            print(f"{camper.get('Nombre')} {camper.get('Apellido')}")
    bandera=True
    while(bandera):
        print("\t1. Salir")
        opc=input()
        if opc.isnumeric():
            bandera=False#Mejorar