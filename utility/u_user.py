import os
from datetime import datetime, timedelta
from auth.auth_jwt import generate_token
from mail.service_email import send_mail
from utility.encrypt import fernetEncrypt


def send_mail_confirm_user(key, json):
    info_for_crypt = {
        "exp": str(datetime.now() + timedelta(hours=2)),
        "uuid": json["id_user"],
    }

    fernet_token = fernetEncrypt(key, info_for_crypt)
    info_token = {"rtx": fernet_token["crypt_hash"], "email": json["email"]}
    token = generate_token(info_token, 2, 0)

    params = {
        "name_user": json["name"],
        "url_confirm_acc": "%sconfirm_acc/%s"
        % (os.getenv("WEB_APPLICATION_URL"), token),
    }

    send_mail(
        "[respponse.com] Confime sua conta.",
        json["email"],
        "confirm_acc.html",
        params,
    )
