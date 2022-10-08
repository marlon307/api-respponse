from fastapi import FastAPI, status, HTTPException
import os, time
from datetime import datetime
from routes import routers

# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException
# from fastapi.exceptions import RequestValidationError

# from middleware.m_valid_cnn_front import request_front
os.environ["TZ"] = "America/Sao_Paulo"
time.time()

app = FastAPI(title="API Respponse")
# CORS(app)


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


@app.get("/", status_code=status.HTTP_200_OK, tags=["API STATUS"])
def home():
    return {
        "message": "Todos os serviços estão ativos.",
        "date": datetime.now(),
        "status": 200,
    }


routers(app)
