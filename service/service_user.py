import ast
import os
from auth.auth_jwt import generate_token
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt, fernetEncrypt, fernetDecrypt
from utility.generat_id import generate_id
from utility.conpare_date import conpare_date
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from mail.service_email import send_mail
from utility.u_user import send_mail_confirm_user


class sUser:
    def s_register_user(json):
        key = Fernet.generate_key()

        json["id_user"] = generate_id()
        json["password"] = encrypt(json["password"])
        json["user_token"] = key
        execut_query.insert(qUser.q_register_user(), json)
        send_mail_confirm_user(key, json)
        return True

    def s_user_confirmacc(json):
        result = execut_query.selectOne(
            qUser.q_select_user_token(), {"email": json["email"], "confirm_acc": False}
        )

        if result is not None and result["user_token"] != json["rtx"]:
            object_decrypt = fernetDecrypt(result["user_token"], json["rtx"])

            if object_decrypt is not False:
                new_object = ast.literal_eval(object_decrypt)

                if conpare_date(new_object["exp"], new_object["exp"]):
                    execut_query.update(
                        qUser.q_update_active_acc(),
                        {
                            "id_user": new_object["uuid"],
                            "email": json["email"],
                            "date": datetime.now(),
                            "user_token": json["rtx"],
                        },
                    )
                    return True
                return False
            return False
        return False

    def s_request_new_confirm_acc(json):
        result = execut_query.selectOne(
            qUser.q_select_emailuser(), {"email": json["email"], "confirm_acc": False}
        )
        if result is not None:
            key = Fernet.generate_key()
            execut_query.update(
                qUser.q_request_update_token(), {"email": result["email"], "key": key}
            )
            json["id_user"] = result["id_user"]
            send_mail_confirm_user(key, json)
            return True
        return False

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
            return False
        return False

    def s_solicitation_user_resetpsw(email):
        key = Fernet.generate_key()

        result = execut_query.selectOne(
            qUser.q_select_emailuser(), {"email": email, "confirm_acc": True}
        )
        execut_query.update(
            qUser.q_request_update_token(), {"email": result["email"], "key": key}
        )

        info_for_crypt = {
            "exp": str(datetime.now() + timedelta(minutes=15)),
            "uuid": result["id_user"],
        }

        fernet_token = fernetEncrypt(key, info_for_crypt)
        info_token = {"rtx": fernet_token["crypt_hash"], "email": result["email"]}
        token = generate_token(info_token, 0, 15)

        params = {
            "url_reset_psw": "%sreset_psw_user/token=%s"
            % (os.getenv("WEB_APPLICATION_URL"), token),
        }
        send_mail(
            "[respponse.com] Solicitção para trocar senha.",
            result["email"],
            "reset_psw.html",
            params,
        )
        return True

    def s_user_resetpsw(data, json):
        result = execut_query.selectOne(
            qUser.q_select_user_token(), {"email": data["email"], "confirm_acc": True}
        )
        if result is not None and result["user_token"] != data["rtx"]:
            object_decrypt = fernetDecrypt(result["user_token"], data["rtx"])
            new_object = ast.literal_eval(object_decrypt)

            if conpare_date(new_object["exp"], new_object["exp"]):
                new_psw = encrypt(json["password"])

                execut_query.update(
                    qUser.q_update_psw_user(),
                    {
                        "password": new_psw,
                        "user_token": data["rtx"],
                        "id_user": new_object["uuid"],
                        "email": data["email"],
                    },
                )
                return True
            return False
        return False
