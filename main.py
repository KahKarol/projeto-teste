"""Projeto no GitHub Actions."""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    """Titulo"""
    return {"message": "Meu primeiro Projeto com Docker!"}

