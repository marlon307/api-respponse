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
        print(query)
        try:
            self.connection = connection.MySQLConnection(**config_connection)
            self.cursor = self.connection.cursor(dictionary=True, buffered=True)
            self.execute = self.cursor.execute
            self.executemany = self.cursor.executemany
            self.callProc = self.cursor.callproc
            self.commit = self.connection.commit
            self.closeCursor = self.cursor.close
            self.closeConnection = self.connection.close
            self.stored_results = self.cursor._stored_results
            self.query = query
        except mysql.connector.Error as errno:
            print("MySQL connector: -> ", errno)
            self.cursor.close()
            self.connection.close()
            raise errno

    def insert(self, data: dict) -> None:
        self.execute(self.query, data)
        id_insert = self.cursor.lastrowid
        self.closeCursor()
        self.commit()
        self.closeConnection()
        return id_insert

    def delete(self, condition: dict) -> None:
        self.execute(self.query, condition)
        self.closeCursor()
        self.commit()
        self.closeConnection()

    def insertMany(self, data: list[dict]) -> list[int]:
        self.executemany(self.query, data)
        # l_id last id
        l_id = self.cursor.lastrowid or 0
        id_insert = [l_id + v for v in range(self.cursor.rowcount)]
        self.closeCursor()
        self.commit()
        self.closeConnection()
        return id_insert

    def update(self, condition: dict) -> None:
        self.execute(self.query, condition)
        self.closeCursor()
        self.commit()
        self.closeConnection()

    def select(self, condition: dict = {}) -> list | None:
        self.execute(self.query, condition)
        result = self.cursor.fetchall()
        self.closeCursor()
        self.closeConnection()
        return result

    def selectOne(self, condition: dict = {}) -> dict | None:
        self.execute(self.query, condition)
        result = self.cursor.fetchone()
        self.closeCursor()
        self.closeConnection()
        return result

    def callProcedure(self, data):
        self.callProc(self.query, data)
        result = list()
        for obj in self.stored_results:
            result = obj.fetchall()
        self.closeCursor()
        self.closeConnection()
        return result
