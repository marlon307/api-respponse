import mysql
from auth.auth_jwt import generate_token
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt
from utility.generat_id import generate_id


class sUser:
    def s_register_user(json):
        json["id_user"] = generate_id()
        json["password"] = encrypt(json["password"])
        execut_query.insert(qUser.q_register_user(), json)
        return True

    def s_login_user(json):
        info_login = execut_query.selectOne(qUser.q_login_user(), json)
        if info_login:

            valid_psw = checkcrypt(json["password"], info_login["password"])
            del info_login["password"]

            if valid_psw:
                token = generate_token(info_login)

                return {
                    "info_login": info_login,
                    "token": token,
                }
            else:
                return False
        else:
            return False

    def s_user_resetpsw(email, token):
        print(email, token)
        return {
            "email": email,
            "token": token,
        }, 200
        # return {
        #     "msg": "ok",
        # }, 200
