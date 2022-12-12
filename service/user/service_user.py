import os
from uuid import uuid4
from auth.auth_jwt import generate_token
from models.database import execut_query
from models import model_user
from utility.encrypt import encrypt, checkcrypt, fernetEncrypt, fernetDecrypt
from utility.format_doc import format_cel, format_cpf, format_email
from utility.conpare_date import conpare_date
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from mail.service_email import send_mail
from utility.u_user import send_mail_confirm_user


def register_user(data):
    info_email = execut_query(model_user.q_login_user).selectOne({"email": data.email})
    if "email" not in info_email:
        key = Fernet.generate_key()
        new_obj = {
            "id_user": uuid4(),
            "name": data.name,
            "email": data.email,
            "password": encrypt(data.password),
            "user_token": key,
        }
        execut_query(model_user.q_register_user).insert(new_obj)
        send_mail_confirm_user(key, new_obj)
        return True
    return False


def login_user(data):
    info_login = execut_query(model_user.q_login_user).selectOne(
        {"email": data.username}
    )
    if "password" in info_login:
        valid_psw = checkcrypt(data.password, info_login["password"])
        if valid_psw is True:
            # Token valido por 6 horas
            if info_login["admin"] == True:
                info_for_crypt = {
                    "exp": str(datetime.now() + timedelta(hours=6)),
                    "admin": info_login["admin"],
                }
                fernet_token = fernetEncrypt(
                    os.getenv("ADMIN_KEY", "").encode("utf8"), info_for_crypt
                )
                info_login["mix"] = fernet_token["crypt_hash"]

            # Nunca passe esse (del) abaixo do (token = generate_token(info_login, 6, 0))
            del info_login["admin"]
            del info_login["password"]
            # (del) proibido ficar abixo do (token = generate_token(info_login,6, 0))

            token = generate_token(info_login, 6, 0)

            return token
        return False
    return False


def user_confirmacc(json: dict):
    result = execut_query(model_user.q_select_user_token).selectOne(
        {"email": json["email"]}
    )

    if result is not None and result["user_token"] != json["rtx"]:
        object_decrypt = fernetDecrypt(result["user_token"], json["rtx"])

        if object_decrypt is not False:
            if conpare_date(object_decrypt["exp"], object_decrypt["exp"]):
                execut_query(model_user.q_update_active_acc).update(
                    {
                        "id_user": object_decrypt["uuid"],
                        "email": json["email"],
                        "date": datetime.now(),
                        "user_token": json["rtx"],
                    }
                )
                return True
            return False
        return False
    return False


def request_new_confirm_acc(email):
    json = execut_query(model_user.q_select_emailuser).selectOne({"email": email})
    if json is not None:
        key = Fernet.generate_key()
        execut_query(model_user.q_request_update_token).update(
            {"email": json["email"], "key": key}
        )
        send_mail_confirm_user(key, json)
        return True
    return False


def solicitation_user_resetpsw(email):
    result = execut_query(model_user.q_select_emailuser).selectOne({"email": email})
    if result is not None:
        key = Fernet.generate_key()
        execut_query(model_user.q_request_update_token).update(
            {"email": result["email"], "key": key}
        )

        info_for_crypt = {
            "exp": str(datetime.now() + timedelta(minutes=15)),
            "uuid": result["id_user"],
        }

        fernet_token = fernetEncrypt(key, info_for_crypt)
        info_token = {"rtx": fernet_token["crypt_hash"], "email": result["email"]}
        token = generate_token(info_token, 0, 15)
        print(token)
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


def user_resetpsw(data):
    result = execut_query(model_user.q_select_user_token).selectOne(
        {"email": data["email"]}
    )
    if result is not None and result["user_token"] != data["rtx"]:
        object_decrypt = fernetDecrypt(result["user_token"], data["rtx"])

        if object_decrypt is not False:
            if conpare_date(object_decrypt["exp"], object_decrypt["exp"]):
                new_psw = encrypt(data["password"])
                execut_query(model_user.q_update_psw_user).update(
                    {
                        "password": new_psw,
                        "user_token": data["rtx"],
                        "id_user": object_decrypt["uuid"],
                        "email": data["email"],
                    },
                )
                return True
            return False
        return False
    return False


def get_info_user(id_user):
    result = execut_query(model_user.q_select_info_user).selectOne({"user_id": id_user})
    return result


def update_info_user(json):
    json["doc"] = format_cpf(json["doc"])
    json["cel"] = format_cel(json["cel"])
    json["tel"] = format_cel(json["tel"])

    execut_query(model_user.q_update_user).update(json)
    return True
