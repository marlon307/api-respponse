from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from routes import routers
from pydantic import BaseModel


app = FastAPI(
    title="API Respponse",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
    },
)

origins = [
    "https://project-respponse-marlon307.vercel.app/",
    "http://localhost:3000",
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
# https://betterprogramming.pub/how-to-build-and-deploy-a-fastapi-task-manager-app-on-vercel-c3aa82b8365e
