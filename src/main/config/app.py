from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.routes import brasileirao_router

app = FastAPI(
    title="API Brasileirão",
    summary="Dados atualizados do campeonato brasileiro",
    version="1.0.0",
    contact={
        "name": "Gustavo Henrique Oliveira dos Santos",
        "url": "https://www.linkedin.com/in/gustavo-henrique-oliveira-dos-santos-028aa4181/",
        "email": "gustavo.henrique.oliveira50@gmail.com"
    },
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(brasileirao_router.router, prefix='/v1', tags=['Campeonato Brasileiro'])
