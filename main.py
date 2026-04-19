"""Módulo de exemplo para GitHub Actions."""
import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """Retorna uma mensagem de boas-vindas."""
    return {"message": "Hello World"}

@app.get("/testei")
async def funcaoteste():
    """Retorna um teste com número aleatório."""
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}

