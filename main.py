"""Modulo principal do projeto para validacao no GitHub Actions."""
import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """Rota raiz que retorna saudacao."""
    return {"message": "Hello World"}

@app.get("/testei")
async def funcaoteste():
    """Rota de teste que retorna um numero aleatorio."""
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}
