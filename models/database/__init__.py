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
            self.cursor = self.connection.cursor(dictionary=True)
            self.execute = self.cursor.execute
            self.commit = self.connection.commit
            self.closeCursor = self.cursor.close
            self.closeConnection = self.connection.close
        except mysql.connector.Error as err:
            # self.connection.close()
            # self.connection.close()
            print(err)

    def insert(query, data):
        cnn = execut_query()
        cnn.execute(query, data)
        cnn.closeCursor()
        cnn.commit()
        cnn.closeConnection()

    def update(query, data):
        cnn = execut_query()
        cnn.execute(query, data)
        cnn.closeCursor()
        cnn.commit()
        cnn.closeConnection()

    def select(query, data):
        cnn = execut_query()
        cnn.execute(query, data)
        result = cnn.cursor.fetchall()
        cnn.closeCursor()
        cnn.closeConnection()
        return result

    def selectOne(query, data):
        cnn = execut_query()
        cnn.execute(query, data)
        result = cnn.cursor.fetchone()
        cnn.closeCursor()
        cnn.closeConnection()
        return result
