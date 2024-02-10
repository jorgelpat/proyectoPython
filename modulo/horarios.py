import json

def ingreso_camper_hora1():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                if len(opc["Campers"])<33:
                    opc["Campers"].append(id)
                else:
                    print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario1.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora1():
    id = input("Indique id del trainer que desea agregar:\n")
    infArea1={
        "Campers": [],
        "Trainer": "",
        "Area": "1"
    }
    infArea1["Trainer"]=id

def ingreso_camper_hora2():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                if len(opc["Campers"])<33:
                    opc["Campers"].append(id)
                else:
                    print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario2.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora2():
    id = input("Indique id del trainer que desea agregar:\n")
    infArea1={
        "Campers": [],
        "Trainer": "",
        "Area": "1"
    }
    infArea1["Trainer"]=id

def ingreso_camper_hora3():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                if len(opc["Campers"])<33:
                    opc["Campers"].append(id)
                else:
                    print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario3.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora3():
    id = input("Indique id del trainer que desea agregar:\n")
    infArea1={
        "Campers": [],
        "Trainer": "",
        "Area": "1"
    }
    infArea1["Trainer"]=id

def ingreso_camper_hora4():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                if len(opc["Campers"])<33:
                    opc["Campers"].append(id)
                else:
                    print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario4.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora4():
    id = input("Indique id del trainer que desea agregar:\n")
    infArea1={
        "Campers": [],
        "Trainer": "",
        "Area": "1"
    }
    infArea1["Trainer"]=id

#Hace falta editar los datos para que se abran con el json