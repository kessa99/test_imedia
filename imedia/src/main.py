"""
fichier principale de lancement du projet
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime

from src.config.init_db import init_db
from src.config.connexion_database import engine
from sqlalchemy import text

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
    try:
        init_db()
    except Exception as e:
        raise RuntimeError(f"Impossible de se connecter à la base de données : {e}")

@app.get("/health", tags=["health"])
def health_check():
    """
    check de la santé de l'application
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "unavailable",
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0",
                "database": "unreachable"
            }
        )

    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "database": db_status
    }