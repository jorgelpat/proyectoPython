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
            else:
                print("Opcion no valida")
        with open("modulo/storage/rutas.json") as f:
            rutas1 = json.loads(f.read())
            f.close()
            rutas1.append(ruta)
        with open("modulo/storage/rutas.json","w") as f:
            data=json.dumps(rutas1, indent=4)
            f.write(data)
            f.close()
            
