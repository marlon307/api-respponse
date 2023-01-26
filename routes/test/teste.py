from fastapi import APIRouter


router = APIRouter(tags=["TESTE"])


@router.post("/teste")
def rota_para_teste_rapido():
    return []
