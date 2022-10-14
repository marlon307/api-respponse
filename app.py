import uvicorn
from fastapi import FastAPI
import os, time
from datetime import datetime
from routes import routers
from pydantic import BaseModel


os.environ["TZ"] = "America/Sao_Paulo"
time.time()

app = FastAPI(title="API Respponse")


class Status(BaseModel):
    datail: str
    date: datetime
    status: int


@app.get("/", response_model=Status, tags=["API STATUS"])
def status():
    return {
        "detail": "Todos os serviços estão ativos.",
        "date": datetime.now(),
        "status": 200,
    }


routers(app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", env_file=".env", reload=True)
