# backend/main.py
import sqlite3
import sys
import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from loguru import logger

# Logging
logger.remove()
logger.add(sys.stdout, serialize=True, enqueue=True)

# Configuración
DB_PATH = "data/tickets.db"
app = FastAPI(title="Corporate EPIS Pilot API - Advanced Flow")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes cambiarlo por tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de intención
class RouteQuery(BaseModel):
    intent: Literal["pregunta_general", "reporte_de_problema", "despedida"] = Field(
        description="La intención del usuario."
    )

# Función para crear ticket
def create_support_ticket(description: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """
    )
    description = description.strip() or "Problema no especificado."
    cursor.execute(
        "INSERT INTO tickets (description, status) VALUES (?, ?)",
        (description, "Abierto"),
    )
    ticket_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return f"Ticket #{ticket_id} creado con: '{description}'"

# Función para clasificar intención de forma simple
def classify_intent(question: str) -> str:
    q = question.lower()
    if any(word in q for word in ["problema", "no funciona", "error", "falla", "computadora", "equipo"]):
        return "reporte_de_problema"
    elif any(word in q for word in ["gracias", "adiós", "vale", "perfecto"]):
        return "despedida"
    else:
        return "pregunta_general"

# Endpoint principal
@app.get("/ask")
def ask_question(question: str):
    try:
        intent = classify_intent(question)
        answer = ""
        follow_up = False

        if intent == "pregunta_general":
            answer = f"Entiendo tu consulta: '{question}'. Te responderé pronto con información útil."
            follow_up = False

        elif intent == "reporte_de_problema":
            ticket_msg = create_support_ticket(question)
            answer = f"He detectado un problema y he creado un ticket automáticamente.\n{ticket_msg}"
            follow_up = True

        elif intent == "despedida":
            answer = "De nada, ¡un placer ayudar! 😊"
            follow_up = False

        return {"answer": answer, "follow_up_required": follow_up}

    except Exception as e:
        logger.error(f"Error en /ask: {e}")
        return {"answer": "Lo siento, ha ocurrido un error.", "follow_up_required": False}

