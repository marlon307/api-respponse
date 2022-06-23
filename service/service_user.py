from flask import jsonify
import mysql
from models.database import cursor, cnn
from models.model_user import qUser


class sUser:
    def register_user(json):
        try:
            cursor.execute(qUser.q_login_user, json)
            cnn.commit()
            cursor.close()
            cnn.close()
            return (
                jsonify(msg="Usuário cadastrado com sucesso! ;)", status=201),
                201,
            )
        except mysql.connector.Error as err:
            if err.errno == 1062:
                return jsonify(msg="Este usuário já possui cadastro.", status=403), 403
            return jsonify(msg="Falha nossa. :(", status=500), 500

    def login_user(json):
        try:
            cursor.execute(qUser.q_login_user(), json)
            info_login = cursor.fetchone()
            # cursor.close()
            # cnn.close()
            return (
                jsonify(
                    user=info_login, msg="Usuário logado com sucesso. ;)", status=200
                ),
                200,
            )
        except mysql.connector.Error as err:
            print(err)
            if err.errno == 1062:
                return jsonify(msg="Este usuário já possui cadastro.", status=403), 403
            return jsonify(msg="Falha nossa. :(", status=500), 500
