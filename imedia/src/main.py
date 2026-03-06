"""
Point d'entrée de l'application
"""

from fastapi import FastAPI

from src.config.init_db import init_db
from src.interface.api.v1.router import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="IMedia",
        description="",
        version="1.0.0",
    )

    app.include_router(router, prefix="/api/v1")

    return app


app = create_app()


@app.on_event("startup")
async def on_startup():
    """Crée les tables en base de données au démarrage"""
    init_db()


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok", "version": "1.0.0"}
