from pymongo import MongoClient
import certifi

MONGO ='mongodb+srv://juliana:<ucundinamarca>@cluster0.kd118a2.mongodb.net/'

certificado = certifi.where()

def Conexion():
    try:
        client =  MongoClient(MONGO, tlsCAFile=certificado)
        bd = client["bd_personas"]
        print("Conexion Exitosa")
    except ConnectionError:
        a = print("Error de Conexion")
    return a

Conexion()