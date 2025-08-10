@app.post("/ask-mock")
async def ask_mock(request: Request):
    data = await request.json()
    user_query = data.get("query", "")
    # Respuesta simulada de OpenAI para pruebas
    return {"response": f"Respuesta simulada de OpenAI a: {user_query}"}
from fastapi import FastAPI, Request
import openai
import os
import requests

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-REEMPLAZAR")
OJS_API_URL = os.getenv("OJS_API_URL", "https://ojs.example.com/api")


@app.post("/ask")
async def ask_ojs(request: Request):
    data = await request.json()
    user_query = data.get("query", "")
    # 1. Consultar OJS (simulado)
    try:
        ojs_response = requests.get(f"{OJS_API_URL}/search", params={"q": user_query}, timeout=10)
        ojs_response.raise_for_status()
        ojs_data = ojs_response.json()
        ojs_summary = ojs_data.get("summary", "No se encontró información relevante en OJS.")
    except Exception:
        ojs_summary = "No se pudo obtener información de OJS."

    # 2. Consultar OpenAI
    try:
        openai.api_key = OPENAI_API_KEY
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en OJS (Open Journal Systems)."},
                {"role": "user", "content": f"Consulta: {user_query}\nResumen OJS: {ojs_summary}"}
            ]
        )
        ai_response = completion.choices[0].message.content.strip()
    except Exception:
        ai_response = f"No se pudo obtener respuesta de OpenAI. Resumen OJS: {ojs_summary}"

    return {"response": ai_response}
