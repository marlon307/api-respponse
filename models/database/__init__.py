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
    def __init__(self, query: str):
        try:
            cnx = connection.MySQLConnection(**config_connection)
            cursor = cnx.cursor(dictionary=True, buffered=True)
            self.cursor = cursor
            self.execute = cursor.execute
            self.executemany = cursor.executemany
            self.callProc = cursor.callproc
            self.commit = cnx.commit
            self.closeCursor = cursor.close
            self.closeConnection = cnx.close
            self.stored_results = cursor._stored_results
            self.query = query
        except mysql.connector.Error as errno:
            # self.cursor.close()
            # self.connection.close()
            raise errno

    def insert(self, data: dict) -> int:
        self.execute(self.query, data)
        id_insert = self.cursor.lastrowid
        self.closeCursor()
        self.commit()
        self.closeConnection()
        return id_insert or 0

    def delete(self, condition: dict) -> None:
        self.execute(self.query, condition)
        self.closeCursor()
        self.commit()
        self.closeConnection()

    def insertMany(self, data: list[dict]) -> list[int]:
        self.executemany(self.query, data)
        # l_id last id
        l_id = self.cursor.lastrowid or 0
        id_insert = [l_id - v for v in range(self.cursor.rowcount)]
        self.closeCursor()
        self.commit()
        self.closeConnection()
        id_insert.sort()
        return id_insert

    def update(self, condition: dict) -> None:
        self.execute(self.query, condition)
        self.closeCursor()
        self.commit()
        self.closeConnection()

    def select(self, condition: dict = {}) -> list:
        self.execute(self.query, condition)
        result = self.cursor.fetchall()
        self.closeCursor()
        self.closeConnection()
        return result or list()

    def selectOne(self, condition: dict = {}) -> dict:
        self.execute(self.query, condition)
        result = self.cursor.fetchone()
        self.closeCursor()
        self.closeConnection()
        return result or dict()

    def callProcedure(self, data):
        self.callProc(self.query, data)
        result = list()
        for obj in self.stored_results:
            result = obj.fetchall()
        self.closeCursor()
        self.closeConnection()
        return result
