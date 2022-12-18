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


class MySQLCnn:
    def __init__(self):
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
            self.stored_results = cursor.stored_results
        except mysql.connector.Error as errno:
            # self.cursor.close()
            # self.connection.close()
            cnx.rollback()
            self.commit()
            self.closeCursor()
            self.closeConnection()
            raise errno

    def insert(self, query: str, data: dict) -> int:
        self.execute(query, data)
        id_insert = self.cursor.lastrowid
        # self.closeCursor()
        # self.commit()
        # self.closeConnection()
        return id_insert or 0

    def insertMany(self, query: str, data: list[dict]) -> list[int]:
        self.executemany(query, data)
        # l_id last id
        l_id = self.cursor.lastrowid or 0
        id_insert = [l_id - v for v in range(self.cursor.rowcount)]
        # self.closeCursor()
        # self.commit()
        # self.closeConnection()
        id_insert.sort()
        return id_insert

    def delete(self, query: str, condition: dict) -> None:
        self.execute(query, condition)
        # self.closeCursor()
        # self.commit()
        # self.closeConnection()

    def update(self, query: str, condition: dict) -> None:
        self.execute(query, condition)
        # self.closeCursor()
        # self.commit()
        # self.closeConnection()

    def select(self, query: str, condition: dict = {}) -> list:
        self.execute(query, condition)
        result = self.cursor.fetchall()
        # self.closeCursor()
        # self.closeConnection()
        return result or list()

    def selectOne(self, query: str, condition: dict = {}) -> dict:
        self.execute(query, condition)
        result = self.cursor.fetchone()
        # self.closeCursor()
        # self.closeConnection()
        return result or dict()

    def callProcedure(self, query: str, data):
        self.callProc(query, data)
        result = list()
        for obj in self.stored_results():
            result = obj.fetchall()
        # self.closeCursor()
        # self.closeConnection()
        return result

    def finishExecution(self):
        self.commit()
        self.closeCursor()
        self.closeConnection()
