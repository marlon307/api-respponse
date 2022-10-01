from fastapi import FastAPI
import os, time
from datetime import datetime
from routes.init_route import routes

# from middleware.m_valid_cnn_front import request_front

os.environ["TZ"] = "America/Sao_Paulo"
time.time()

app = FastAPI()
# CORS(app)
routes(app)


@app.get("/")
def home():
    res = {
        "message": "Todos os serviços estão ativos.",
        "date": datetime.now(),
        "status": 200,
    }

    return res
