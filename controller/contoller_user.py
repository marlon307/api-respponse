from flask import request
from service.service_user import sUser
from flask import jsonify


class cUser:
    def c_user_register():
        try:
            json = request.get_json()
            sUser.s_register_user(json)

            return (
                jsonify(msg="Usuário cadastrado com sucesso!", status=201),
                201,
            )
        except Exception as err:
            if err.errno == 1062:
                return jsonify(msg="Este usuário já possui cadastro.", status=403), 403
            print(err)
            return jsonify(msg="Falha nossa.", status=500), 500

    def c_user_login():
        try:
            json = request.get_json()
            result = sUser.s_login_user(json)
            if result:
                return (
                    jsonify(
                        user=result["info_login"],
                        msg="Usuário logado com sucesso.",
                        token=result["token"],
                        status=200,
                    ),
                    200,
                )
            else:
                return {"msg": "Dados Inválidos.", "status": 400}, 400
        except Exception as err:
            print(err)
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
            print(err)
            return {"msg": "Dados Inválidos.", "status": 400}, 400

    def c_user_resetpsw():
        result = sUser.s_user_resetpsw(request.headers)
        return {"ok": result}
