from base64 import encode
from datetime import datetime, timedelta
from flask import request, jsonify
from service.service_user import sUser


class cUser:
    def c_user_register():
        try:
            json = request.get_json()
            sUser.s_register_user(json)

            return {"msg": "Confime sua conta.", "status": 201}, 201
        except Exception as err:
            if err.errno == 1062:
                return {"msg": "Este usuário já possui cadastro.", "status": 403}, 403
            print("c_user_register ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_user_confirmacc():
        try:
            reult = sUser.s_user_confirmacc(request.headers["user"])
            if reult:
                return {"msg": "Conta confimarda.", "status": 200}, 200
            return {"msg": "Conta já confirmada ou não existe.", "status": 400}, 400
        except Exception as err:
            print("c_user_confirmacc ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

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
            print("c_request_new_confirm_acc ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_user_login():
        try:
            json = request.get_json()
            result = sUser.s_login_user(json)
            if result:
                new_json = jsonify(
                    user=result["info_login"],
                    msg="Usuário logado com sucesso.",
                    token=result["token"],
                    status=200,
                )
                date_time = datetime.now() + timedelta(hours=6 + 3)
                exp = date_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
                new_json.set_cookie(
                    "u_token",
                    result["token"],
                    expires=exp,
                    secure=True,
                    samesite="Strict",
                    httponly=True,
                )
                return new_json, 200
            else:
                return {"msg": "Dados Inválidos.", "status": 400}, 400
        except Exception as err:
            print("c_user_login ->", err)
            return {"msg": "Dados Inválidos.", "status": 400}, 400

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
            print("c_solicitation_user_resetpsw ->", err)
            return {"msg": "Dados Inválidos.", "status": 400}, 400

    def c_user_resetpsw():
        try:
            json = request.get_json()
            result = sUser.s_user_resetpsw(request.headers["user"], json)
            if result:
                return {"msg": "Senha alterada com sucesso.", "status": 200}, 200
            return {"msg": "Senha já alterada com este token.", "status": 400}, 400

        except Exception as err:
            print("c_user_resetpsw ->", err)
            return {"msg": "Dados Inválidos.", "status": 400}, 400
