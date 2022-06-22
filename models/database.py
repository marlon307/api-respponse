import os
from mysql.connector import connection

config_connection = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PSW"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}

cnn = connection.MySQLConnection(**config_connection)

cursor = cnn.cursor(dictionary=True)


# cnn.close()
