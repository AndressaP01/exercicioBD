
import pymongo
from pymongo import MongoClient

class Database:
    def __init__(self):
        cluster = MongoClient("mongodb+srv://anddessa01:7mbjkppq@cluster0.geibsck.mongodb.net/test")
        self.db = cluster["cluster_atlas_exercicio_avaliativo"]
        self.collection = self.db["Motorista"]




