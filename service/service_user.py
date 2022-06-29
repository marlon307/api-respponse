from auth.auth_jwt import generate_token
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt
from utility.generat_id import generate_id
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import ast


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
                # Token valido por 6 horas
                token = generate_token(info_login, 6, 0)

                return {
                    "info_login": info_login,
                    "token": token,
                }
            else:
                return False
        else:
            return False

    def s_solicitation_user_resetpsw(email):
        key = Fernet.generate_key()
        cyper = Fernet(key)

        result = execut_query.selectOne(qUser.q_select_emailuser(), {"email": email})
        execut_query.update(
            qUser.q_request_rest_psw(), {"email": result["email"], "key": key}
        )

        info_for_crypt = {
            "exp": str(datetime.now() + timedelta(minutes=15)),
            "uuid": result["id_user"],
        }

        encrypt = cyper.encrypt(str(info_for_crypt).encode("utf-8"))
        info_token = {"rtx": encrypt.decode("utf-8"), "email": result["email"]}
        token = generate_token(info_token, 0, 15)
        print(token)
        return True

    def s_user_resetpsw(data):
        result = execut_query.selectOne(
            qUser.q_select_k_userpsw(), {"email": data["email"]}
        )

        if result["key_resetpsw"] != data["rtx"]:
            cyper = Fernet(str(result["key_resetpsw"]).encode("utf-8"))
            decrypt = cyper.decrypt(str(data["rtx"]).encode("utf-8"))
            object_decrypt = decrypt.decode("utf-8")

            new_psw = encrypt("123A3dq?")

            execut_query.update(
                qUser.q_update_psw_user(),
                {
                    "password": new_psw,
                    "key_resetpsw": data["rtx"],
                    "id_user": ast.literal_eval(object_decrypt)["uuid"],
                    "email": data["email"],
                },
            )

            return True
        return False
