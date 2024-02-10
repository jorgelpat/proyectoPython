import json

def ingreso_camper_hora1_area1():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
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

def ingreso_trainer_hora1_area1():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                opc["Trainer"]=id
    with open("modulo/storage/horario1.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





def ingreso_camper_hora2_area1():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
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

def ingreso_trainer_hora2_area1():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                opc["Trainer"]=id
    with open("modulo/storage/horario2.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





def ingreso_camper_hora3_area1():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
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

def ingreso_trainer_hora3_area1():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                opc["Trainer"]=id
    with open("modulo/storage/horario3.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





def ingreso_camper_hora4_area1():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
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

def ingreso_trainer_hora4_area1():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="1":
                opc["Trainer"]=id
    with open("modulo/storage/horario4.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"




def ingreso_camper_hora1_area2():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="2":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario1.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora1_area2():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="2":
                opc["Trainer"]=id
    with open("modulo/storage/horario1.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"




def ingreso_camper_hora2_area2():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="2":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario2.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora2_area2():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="2":
                opc["Trainer"]=id
    with open("modulo/storage/horario2.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"




def ingreso_camper_hora3_area2():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="2":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario3.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora3_area2():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="2":
                opc["Trainer"]=id
    with open("modulo/storage/horario3.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"




def ingreso_camper_hora4_area2():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="2":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario4.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora4_area2():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="2":
                opc["Trainer"]=id
    with open("modulo/storage/horario4.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





def ingreso_camper_hora4_area3():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="3":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario4.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora4_area3():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario4.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="3":
                opc["Trainer"]=id
    with open("modulo/storage/horario4.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





def ingreso_camper_hora1_area3():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="3":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario1.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora1_area3():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario1.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="3":
                opc["Trainer"]=id
    with open("modulo/storage/horario1.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





def ingreso_camper_hora2_area3():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="3":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario2.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora2_area3():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario2.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="3":
                opc["Trainer"]=id
    with open("modulo/storage/horario2.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"




def ingreso_camper_hora3_area3():
    id = input("Indique id del camper: ")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        with open("modulo/storage/camper.json") as f1:
            campers=json.loads(f1.read())
            for camper in campers:
                if camper["Estado"]=="Aprobado" and camper["Id"]==id:
                    for opc in horario:
                        if opc["Area"]=="3":
                            if len(opc["Campers"])<33:
                                opc["Campers"].append(id)
                            else:
                                print("Ya hay un maximo de 33 campers")
    with open("modulo/storage/horario3.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Campers Agregados"

def ingreso_trainer_hora3_area3():
    id = input("Indique id del trainer que desea agregar:\n")
    with open("modulo/storage/horario3.json") as f:
        horario=json.loads(f.read())
        for opc in horario:
            if opc["Area"]=="3":
                opc["Trainer"]=id
    with open("modulo/storage/horario3.json","w") as f:
        horario=json.dumps(horario,indent=4)
        f.write(horario)
        f.close()
    return "Trainer Agregado"





