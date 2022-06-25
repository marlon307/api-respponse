from flask import jsonify
import mysql
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt
from utility.generat_id import generate_id


class sUser:
    def register_user(json):
        try:
            json["id_user"] = generate_id()
            json["password"] = encrypt(json["password"])

            execut_query.insert(qUser.q_register_user(), json)
            return (
                jsonify(msg="Usuário cadastrado com sucesso!", status=201),
                201,
            )
        except mysql.connector.Error as err:
            if err.errno == 1062:
                return jsonify(msg="Este usuário já possui cadastro.", status=403), 403
            print(err)
            return jsonify(msg="Falha nossa. :(", status=500), 500

    def login_user(json):
        try:

            info_login = execut_query.selectOne(qUser.q_login_user(), json)
            valid_psw = checkcrypt(json["password"], info_login["password"])
            del info_login["password"]

            if valid_psw:
                return (
                    jsonify(
                        user=info_login, msg="Usuário logado com sucesso.", status=200
                    ),
                    200,
                )

            else:
                return jsonify(msg="Dados Inválidos.", status=400), 400
        except mysql.connector.Error as err:
            print(err)
            if err.errno:
                return jsonify(msg="Falha nossa. :(", status=403), 403
            print(err)
            return jsonify(msg="Falha nossa. :(", status=500), 500
