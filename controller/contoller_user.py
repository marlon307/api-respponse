from flask import request
from service.service_user import sUser


class cUser:
    def c_user_register():
        json = request.get_json()
        result = sUser.s_register_user(json)
        return result

    def c_user_login():
        json = request.get_json()
        result = sUser.s_login_user(json)
        return result

    def c_user_resetpsw(email, token):
        # json = request.get_json()
        result = sUser.s_user_resetpsw(email, token)
        return result
