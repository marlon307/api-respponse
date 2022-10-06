from datetime import datetime, timedelta
from flask import request, jsonify
from service.user.service_user import sUser

msgErr500 = {"msg": "Server error.", "status": 500}, 500


class cUser:
    def c_user_register(body):
        try:
            sUser.s_register_user(body)

            return {"msg": "Confime sua conta.", "status": 201}, 201
        except Exception as err:
            if err.errno == 1062:
                return {"msg": "Este usuário já possui cadastro.", "status": 409}, 409
            print("user -> c_user_register ->", err)
            return msgErr500

    def c_user_confirmacc():
        try:
            reult = sUser.s_user_confirmacc(request.headers["user"])
            if reult:
                return {"msg": "Conta confimarda.", "status": 200}, 200
            return {"msg": "Conta já confirmada ou não existe.", "status": 400}, 400
        except Exception as err:
            print("user -> c_user_confirmacc ->", err)
            return msgErr500

    def c_request_new_confirm_acc():
        try:
            json = request.get_json()
            reult = sUser.s_request_new_confirm_acc(json)
            if reult:
                return {
                    "msg": "Novo email enviado para confirmar conta.",
                    "status": 200,
                }, 200
            return {"msg": "Conta já confirmada ou não existe.", "status": 400}, 400
        except Exception as err:
            print("user -> c_request_new_confirm_acc ->", err)
            return msgErr500

    def c_user_login(data):
        try:
            result = sUser.s_login_user(data)
            if result:
                date_time = datetime.now() + timedelta(hours=6 + 3)
                new_json = jsonify(
                    user=result["info_login"],
                    msg="Usuário logado com sucesso.",
                    token=result["token"],
                    exp=date_time,
                    status=200,
                )
                return new_json, 200
            else:
                return {"msg": "Dados Inválidos.", "status": 400}, 400
        except Exception as err:
            print("user -> c_user_login ->", err)
            return msgErr500

    def c_solicitation_user_resetpsw():
        try:
            json = request.get_json()
            result = sUser.s_solicitation_user_resetpsw(json["email"])

            if result:
                return {
                    "msg": "Email enviado com sucesso.",
                    "status": 200,
                }, 200
            return {"msg": "Dados Inválidos.", "status": 400}, 400
        except Exception as err:
            print("user -> c_solicitation_user_resetpsw ->", err)
            return msgErr500

    def c_user_resetpsw():
        try:
            json = request.get_json()
            result = sUser.s_user_resetpsw(request.headers["user"], json)
            if result:
                return {"msg": "Senha alterada com sucesso.", "status": 200}, 200
            return {"msg": "Senha já alterada com este token.", "status": 400}, 400

        except Exception as err:
            print("user -> c_user_resetpsw ->", err)
            return msgErr500

    def c_get_info_user():
        try:
            id_user = request.headers["user"]["id_user"]
            data = sUser.s_get_info_user(id_user)

            if data:
                return {
                    "msg": "User info.",
                    "status": 200,
                    "response": data,
                }, 200
            return {"msg": "Usuario inexistente!", "status": 400}, 400

        except Exception as err:
            print("user -> c_get_info_user ->", err)
            return msgErr500

    def c_update_info_user():
        try:
            json = request.get_json()
            json["u_id"] = request.headers["user"]["id_user"]
            data = sUser.s_update_info_user(json)

            if data:
                return {
                    "msg": "Usuário atualizado.",
                    "status": 200,
                }, 200
            return {"msg": "Usuario inexistente!", "status": 400}, 400

        except Exception as err:
            print("user -> c_update_info_user ->", err)
            return msgErr500
