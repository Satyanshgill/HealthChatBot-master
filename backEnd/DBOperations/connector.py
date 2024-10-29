import mysql.connector
from decouple import config

class Connector:
    def __init__(self):
        return

    def createConnection(self):
        dbObj = mysql.connector.connect(
            host="localhost",
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            port=3306,
            database="health_fitness"
        )
        return dbObj