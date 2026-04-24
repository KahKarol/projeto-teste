"""Projeto de Data e Hora com FastAPI."""
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI(title="API de Data e Hora")

@app.get("/agora")
def obter_data_hora():
    # Coleta a data e hora 
    agora = datetime.now()

    # Define o fuso horário
    tz = pytz.timezone('America/Sao_Paulo')
    agora = datetime.now(tz)
    
    # Formatação da data
    data_formatada = agora.strftime("%d/%m/%Y")
    hora_formatada = agora.strftime("%H:%M:%S")
    
    # Retorna a resposta
    return {
        "mensagem": f"Hoje é dia {data_formatada} e o horário atual é {hora_formatada}.",
        "data": data_formatada,
        "horario": hora_formatada
    }


