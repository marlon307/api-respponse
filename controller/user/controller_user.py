from fastapi import status, HTTPException
from datetime import datetime, timedelta
from service.user import service_user

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def user_register(body):
    try:
        result = service_user.register_user(body)
        if result is True:
            return {"detail": "Confime sua conta.", "status": 201}
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Este usuário já possui cadastro.",
        )
    except Exception as err:
        print("user -> c_user_register ->", err)
        raise msgErr500


def user_confirmacc(data):
    try:
        reult = service_user.user_confirmacc(data)
        if reult:
            return {"detail": "Conta confimarda.", "status": 200}
        return {"detail": "Conta já confirmada ou não existe.", "status": 400}
    except Exception as err:
        print("user -> c_user_confirmacc ->", err)
        raise msgErr500


def request_new_confirm_acc(data):
    try:
        reult = service_user.request_new_confirm_acc(data["email"])
        if reult:
            return {
                "detail": "Novo email enviado para confirmar conta.",
                "status": 200,
            }
        return {"detail": "Conta já confirmada ou não existe.", "status": 400}
    except Exception as err:
        print("user -> c_request_new_confirm_acc ->", err)
        raise msgErr500


def user_login(data):
    result = service_user.login_user(data)
    if result is not False:
        date_time = datetime.now() + timedelta(hours=6 + 3)
        new_json = {
            "access_token": result["token"],
            "token_type": "bearer",
            "user": result["info_login"],
            "detail": "Usuário logado com sucesso.",
            "exp": date_time,
            "status": 200,
        }
        return new_json
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect e-mail or password",
            headers={"WWW-Authenticate": "Bearer"},
        )


def solicitation_user_resetpsw(data):
    try:
        result = service_user.solicitation_user_resetpsw(data.email)
        if result is True:
            return {
                "detail": "Email enviado com sucesso.",
                "status": 200,
            }
        return {"detail": "Dados Inválidos.", "status": 400}
    except Exception as err:
        print("user -> c_solicitation_user_resetpsw ->", err)
        raise msgErr500


def user_resetpsw(data):
    status_err = None
    try:
        result = service_user.user_resetpsw(data)

        if result is True:
            return {"detail": "Senha alterada com sucesso.", "status": 200}
        status_err = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha já alterada com este token.",
        )
    except Exception as err:
        print("user -> c_user_resetpsw ->", err)
        raise msgErr500
    raise status_err


def get_info_user(data):
    status_err = None
    try:
        data = service_user.get_info_user(data.id_user)
        if data:
            return {
                "detail": "User info.",
                "status": 200,
                "response": data,
            }
        status_err = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inexistente!",
        )

    except Exception as err:
        print("user -> c_get_info_user ->", err)
        raise msgErr500
    raise status_err


def update_info_user(data_json):
    try:
        data = service_user.update_info_user(data_json)

        if data:
            return {
                "detail": "Usuário atualizado.",
                "status": 200,
            }
        return {"detail": "Usuario inexistente!", "status": 400}

    except Exception as err:
        print("user -> c_update_info_user ->", err)
        raise msgErr500
