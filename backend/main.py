from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import conversao

app = FastAPI(title="API Ilumeo — Taxa de Conversão")

# Libera requisições do frontend (se necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra rota
app.include_router(conversao.router)
