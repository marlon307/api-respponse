# import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os, time
from datetime import datetime
from routes import routers
from pydantic import BaseModel

os.environ["TZ"] = "America/Sao_Paulo"
time.time()

app = FastAPI(
    title="API Respponse", swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StatusModel(BaseModel):
    datail: str
    date: datetime
    status: int


@app.get("/", response_model=StatusModel, tags=["API STATUS"])
def status():
    return {
        "datail": "Todos os serviços estão ativos.",
        "date": datetime.now(),
        "status": 200,
    }

routers(app)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", env_file=".env", reload=True)
