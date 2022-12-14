from datetime import datetime, timedelta
from fastapi import status, HTTPException
from service.user import service_user
from utility.handleErr import handlerErr, JSONResponse


def user_register(body, task):
    try:
        result = service_user.register_user(body, task)
        if result is True:
            return {"detail": "Confime sua conta.", "status": 201}
        return JSONResponse(
            content={
                "detail": "Este usuário já possui cadastro.",
                "status": status.HTTP_409_CONFLICT,
            },
            status_code=status.HTTP_409_CONFLICT,
        )
    except Exception as err:
        raise handlerErr("user -> c_user_register -> %s" % err)


def user_confirmacc(data):
    try:
        reult = service_user.user_confirmacc(data)
        if reult:
            return {"detail": "Conta confimarda.", "status": 200}
        return {"detail": "Conta já confirmada ou não existe.", "status": 400}
    except Exception as err:
        raise handlerErr("user -> c_user_confirmacc -> %s" % err)


def request_new_confirm_acc(data):
    try:
        reult = service_user.request_new_confirm_acc(data.email)
        if reult:
            return {
                "detail": "Novo email enviado para confirmar conta.",
                "status": 200,
            }
        return {"detail": "Conta já confirmada ou não existe.", "status": 400}
    except Exception as err:
        raise handlerErr("user -> c_request_new_confirm_acc -> %s" % err)


def user_login(data):
    token = service_user.login_user(data)
    if token is not False:
        date_time = datetime.now() + timedelta(hours=6 + 3)
        new_json = {
            "access_token": token,
            "token_type": "bearer",
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


def solicitation_user_resetpsw(data, tasks):
    try:
        result = service_user.solicitation_user_resetpsw(data.email, tasks)
        if result is True:
            return {
                "detail": "Email enviado com sucesso.",
                "status": 200,
            }
        return {"detail": "Dados Inválidos.", "status": 400}
    except Exception as err:
        raise handlerErr("user -> c_solicitation_user_resetpsw -> %s" % err)


def user_resetpsw(data):
    status_err = None
    try:
        result = service_user.user_resetpsw(data)

        if result is True:
            return {"detail": "Senha alterada com sucesso.", "status": 200}
        status_err = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha já alterada com este token ou inválido.",
        )
    except Exception as err:
        raise handlerErr("user -> c_user_resetpsw -> %s" % err)
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
        raise handlerErr("user -> c_get_info_user -> %s" % err)
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
        raise handlerErr("user -> c_update_info_user -> %s" % err)
