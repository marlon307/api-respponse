from auth.auth_jwt import generate_token
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt
from utility.generat_id import generate_id
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import ast
import os
from mail.service_email import send_mail


class sUser:
    def s_register_user(json):
        key = Fernet.generate_key()

        json["id_user"] = generate_id()
        json["password"] = encrypt(json["password"])
        json["user_token"] = key
        execut_query.insert(qUser.q_register_user(), json)

        info_for_crypt = {
            "exp": str(datetime.now() + timedelta(minutes=15)),
            "uuid": json["id_user"],
        }

        cyper = Fernet(key)
        genertate_hash = cyper.encrypt(str(info_for_crypt).encode("utf-8"))
        info_token = {"rtx": genertate_hash.decode("utf-8"), "email": json["email"]}
        token = generate_token(info_token, 0, 15)

        params = {
            "name_user": json["name"],
            "url_confirm_acc": "%sconfirm_acc/token=%s"
            % (os.getenv("WEB_APPLICATION_URL"), token),
        }

        send_mail(
            "[respponse.com] Confime sua conta.",
            json["email"],
            "confirm_acc.html",
            params,
        )
        return True

    def c_user_confirmacc(json):
        result = execut_query.selectOne(
            qUser.q_select_emailuser(), {"email": json["email"]}
        )
        execut_query.update(
            qUser.q_update_active_acc(), {"email": result["email"], "key": json["key"]}
        )
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
            qUser.q_select_k_userpsw(), {"email": data["email"]}
        )
        if result["user_token"] != data["rtx"]:
            cyper = Fernet(str(result["user_token"]).encode("utf-8"))
            decrypt = cyper.decrypt(str(data["rtx"]).encode("utf-8"))
            object_decrypt = decrypt.decode("utf-8")
            # Transforma minha string em objeto
            new_object = ast.literal_eval(object_decrypt)
            if datetime.fromisoformat(
                new_object["exp"]
            ) >= datetime.now() and datetime.now() <= datetime.fromisoformat(
                new_object["exp"]
            ):
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
