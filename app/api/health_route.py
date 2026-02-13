from fastapi import APIRouter

from app.db.mongodb import database

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    """
    Basic health check
    """
    return {"status": "ok"}


@router.get("/health/db")
async def db_health_check():
    """
    Database connectivity check
    """
    try:
        await database.command("ping")
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": "disconnected", "detail": str(e)}
