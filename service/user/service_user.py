import os
from auth.auth_jwt import generate_token
from models.database import execut_query
from models import model_user
from utility.encrypt import encrypt, checkcrypt, fernetEncrypt, fernetDecrypt
from utility.format_doc import format_cel, format_cpf
from utility.generat_id import generate_id
from utility.conpare_date import conpare_date
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from mail.service_email import send_mail
from utility.u_user import send_mail_confirm_user


def register_user(data):
    key = Fernet.generate_key()
    new_obj = {
        "id_user": generate_id(),
        "name": data.name,
        "email": data.email,
        "password": encrypt(data.password),
        "user_token": key,
    }
    execut_query().insert(model_user.q_register_user, new_obj)
    send_mail_confirm_user(key, new_obj)
    return True


def login_user(data):
    info_login = execut_query().selectOne(
        model_user.q_login_user, {"email": data.username}
    )

    if info_login is not None:
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

            if "mix" in info_login:
                del info_login["mix"]

            return {
                "info_login": info_login,
                "token": token,
            }
        return False
    return False


def user_confirmacc(json: dict):
    result = execut_query().selectOne(
        model_user.q_select_user_token, {"email": json["email"]}
    )

    if result is not None and result["user_token"] != json["rtx"]:
        object_decrypt = fernetDecrypt(result["user_token"], json["rtx"])

        if object_decrypt is not False:
            if conpare_date(object_decrypt["exp"], object_decrypt["exp"]):
                execut_query().update(
                    model_user.q_update_active_acc,
                    {
                        "id_user": object_decrypt["uuid"],
                        "email": json["email"],
                        "date": datetime.now(),
                        "user_token": json["rtx"],
                    },
                )
                return True
            return False
        return False
    return False


def request_new_confirm_acc(email):
    json = execut_query().selectOne(model_user.q_select_emailuser, {"email": email})
    if json is not None:
        key = Fernet.generate_key()
        execut_query().update(
            model_user.q_request_update_token, {"email": json["email"], "key": key}
        )
        send_mail_confirm_user(key, json)
        return True
    return False


def solicitation_user_resetpsw(email):
    result = execut_query().selectOne(model_user.q_select_emailuser, {"email": email})
    if result is not None:
        key = Fernet.generate_key()
        execut_query().update(
            model_user.q_request_update_token, {"email": result["email"], "key": key}
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
    result = execut_query().selectOne(
        model_user.q_select_user_token, {"email": data["email"]}
    )
    if result is not None and result["user_token"] != data["rtx"]:
        object_decrypt = fernetDecrypt(result["user_token"], data["rtx"])

        if object_decrypt is not False:
            if conpare_date(object_decrypt["exp"], object_decrypt["exp"]):
                new_psw = encrypt(data["password"])
                execut_query().update(
                    model_user.q_update_psw_user,
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
    result = execut_query().selectOne(
        model_user.q_select_info_user, {"user_id": id_user}
    )
    return result


def update_info_user(json):
    json["doc"] = format_cpf(json["doc"])
    json["cel"] = format_cel(json["cel"])
    json["tel"] = format_cel(json["tel"])

    execut_query().update(model_user.q_update_user, json)
    return True
