from fastapi import FastAPI, status
import os, time
from datetime import datetime
from routes.init_route import routes

# from middleware.m_valid_cnn_front import request_front

os.environ["TZ"] = "America/Sao_Paulo"
time.time()

app = FastAPI()
# CORS(app)
routes(app)


@app.get("/", status_code=status.HTTP_200_OK, tags=["API STATUS"])
def home():
    return {
        "message": "Todos os serviços estão ativos.",
        "date": datetime.now(),
        "status": 200,
    }
