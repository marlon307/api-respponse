import ast
import os
from auth.auth_jwt import generate_token
from models.database import execut_query
from models.model_user import qUser
from utility.encrypt import encrypt, checkcrypt, fernetEncrypt, fernetDecrypt
from utility.format_doc import format_cel, format_cpf
from utility.generat_id import generate_id
from utility.conpare_date import conpare_date
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from mail.service_email import send_mail
from utility.u_user import send_mail_confirm_user


class sUser:
    def s_register_user(json):
        key = Fernet.generate_key()
        new_obj = {
            "id_user": generate_id(),
            "name": json.name,
            "email": json.email,
            "password": encrypt(json.password),
            "user_token": key,
        }
        execut_query.insert(qUser.q_register_user(), new_obj)
        send_mail_confirm_user(key, new_obj)
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

    def s_request_new_confirm_acc(email):
        json = execut_query.selectOne(qUser.q_select_emailuser(), {"email": email})
        if json is not None:
            key = Fernet.generate_key()
            execut_query.update(
                qUser.q_request_update_token(), {"email": json["email"], "key": key}
            )
            send_mail_confirm_user(key, json)
            return True
        return False

    def s_login_user(json):
        info_login = execut_query.selectOne(
            qUser.q_login_user(), {"email": json.username}
        )

        if info_login is not None:
            valid_psw = checkcrypt(json.password, info_login["password"])
            if valid_psw is True:
                # Token valido por 6 horas
                if info_login["admin"] == True:
                    info_for_crypt = {
                        "exp": str(datetime.now() + timedelta(hours=6)),
                        "admin": info_login["admin"],
                    }
                    fernet_token = fernetEncrypt(
                        os.getenv("ADMIN_KEY").encode("utf8"), info_for_crypt
                    )
                    info_login["mix"] = fernet_token["crypt_hash"]

                # Nunca passe esse (del) abaixo do (token = generate_token(info_login, 6, 0))
                del info_login["admin"]
                del info_login["password"]
                # (del) proibido ficar abixo do (token = generate_token(info_login,6, 0))

                token = generate_token(info_login, 6, 0)

                if "mix" in info_login:
                    del info_login["mix"]

                return {
                    "info_login": info_login,
                    "token": token,
                }
            return False
        return False

    def s_solicitation_user_resetpsw(email):
        result = execut_query.selectOne(qUser.q_select_emailuser(), {"email": email})

        if result is not None:
            key = Fernet.generate_key()
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
                "url_reset_psw": "%sreset_psw/%s"
                % (os.getenv("WEB_APPLICATION_URL"), token),
            }
            send_mail(
                "[respponse.com] Solicitção para trocar senha.",
                result["email"],
                "reset_psw.html",
                params,
            )
            return True
        return False

    def s_user_resetpsw(data, json):
        result = execut_query.selectOne(
            qUser.q_select_user_token(), {"email": data["email"], "confirm_acc": True}
        )
        if result is not None and result["user_token"] != data["rtx"]:
            object_decrypt = fernetDecrypt(result["user_token"], data["rtx"])

            if object_decrypt is not False:
                new_object = ast.literal_eval(object_decrypt or "{'exp': 0}")

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
        return False

    def s_get_info_user(id_user):
        result = execut_query.selectOne(
            qUser.q_select_info_user(), {"user_id": id_user}
        )
        return result

    def s_update_info_user(json):
        json["doc"] = format_cpf(json["doc"])
        json["cel"] = format_cel(json["cel"])
        json["tel"] = format_cel(json["tel"])

        execut_query.update(qUser.q_update_user(), json)
        return True
