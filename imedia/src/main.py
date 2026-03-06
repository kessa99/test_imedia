"""
fichier principale de lancement du projet
"""

from fastapi import FastAPI, Request, status
from datetime import datetime

from src.config.init_db import init_db

app = FastAPI()

def create_app():
    """
    creation de l'application
    """

    app = FastAPI(
        title="IMedia",
        description="",
        version="1.0.0"
    )

    return app
app = create_app()

@app.on_event("startup")
async def database_connection():
    """
    connexion à la base de données
    """
    init_db()

@app.get("/health", tags=["health"])
def health_check():
    """
    check de la santé de l'application
    """
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "database": "connected"
    }