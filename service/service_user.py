from auth.auth_jwt import generate_token
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt
from utility.generat_id import generate_id
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime, timedelta


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

    def s_user_resetpsw(email, token):
        # byte_key = bytes(token, "UTF-8")
        # value = hmac.new(byte_key, b"Teste", hashlib.sha256).hexdigest()
        # # hmac.digest(value)
        # print(email, value, b"Teste")
        # teste2 = str(datetime.now()).encode("utf-8")

        key = Fernet.generate_key()
        cyper = Fernet(key)
        teste2 = cyper.encrypt(b"Teste")
        # # teste3 = cyper.decrypt(teste2)

        # print(teste2)
        # hashlib.sha1((token).encode("utf-8")).hexdigest()

        result = execut_query.selectOne(qUser.q_select_emailuser(), {"email": email})
        execut_query.update(
            qUser.q_request_rest_psw(),
            {"email": result["email"], "key": key},
        )

        # print(datetime.now() + timedelta(minutes=15) > datetime.now())

        # teste7 = {"rtx": str(teste2)}
        # token = generate_token(teste7, 0, 1)
        return {
            "token": email,
        }, 200
        # return {
        #     "msg": "ok",
        # }, 200
