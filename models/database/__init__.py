import os
import mysql.connector
from mysql.connector import connection

config_connection = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PSW"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}


class execut_query:
    def __init__(self):
        try:
            self.connection = connection.MySQLConnection(**config_connection)
            self.cursor = self.connection.cursor(dictionary=True, buffered=True)
            self.execute = self.cursor.execute
            self.callProc = self.cursor.callproc
            self.executemany = self.cursor.executemany
            self.commit = self.connection.commit
            self.closeCursor = self.cursor.close
            self.closeConnection = self.connection.close
        except mysql.connector.Error as err:
            print(err)
            # self.cursor.close()
            # self.connection.close()

    def insert(self, query: str, data: dict) -> None:
        self.execute(query, data)
        id_insert = self.cursor.lastrowid
        self.closeCursor()
        self.commit()
        self.closeConnection()
        return id_insert

    def delete(self, query: str, data) -> None:
        self.execute(query, data)
        self.closeCursor()
        self.commit()
        self.closeConnection()

    def insertMany(self, query: str, data: list) -> list[int]:
        self.executemany(query, data)
        id_insert = [self.cursor.lastrowid + v for v in range(self.cursor.rowcount)]
        self.closeCursor()
        self.commit()
        self.closeConnection()
        return id_insert

    def update(self, query: str, data) -> None:
        self.execute(query, data)
        self.closeCursor()
        self.commit()
        self.closeConnection()

    def select(self, query: str, data) -> list | None:
        self.execute(query, data)
        result = self.cursor.fetchall()
        self.closeCursor()
        self.closeConnection()
        return result

    def selectOne(self, query: str, data) -> dict | None:
        self.execute(query, data)
        result = self.cursor.fetchone()
        self.closeCursor()
        self.closeConnection()
        return result

    def callProcedure(self, procedure_name: str, data):
        self.callProc(procedure_name, data)
        result = list()
        for obj in self.cursor.stored_results():
            result = obj.fetchall()
        self.closeCursor()
        self.closeConnection()
        return result
