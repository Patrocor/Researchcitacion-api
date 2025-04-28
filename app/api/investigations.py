from fastapi import APIRouter, HTTPException, Query
from app.database.db import SessionLocal
from app.database.models import Investigation

router = APIRouter(prefix="/api", tags=["Investigations"])

@router.get("/investigations")
async def get_investigations():
    db = SessionLocal()
    investigations = db.query(Investigation).all()
    db.close()

    return [
        {
            "id": inv.id,
            "topic": inv.topic,
            "internal_sections": inv.internal_sections,
            "filename": inv.filename,
            "paragraphs": inv.paragraphs,
            "citations_count": inv.citations_count,
            "created_at": inv.created_at
        }
        for inv in investigations
    ]

@router.get("/investigations/{investigation_id}")
async def get_investigation_by_id(investigation_id: int):
    db = SessionLocal()
    investigation = db.query(Investigation).filter(Investigation.id == investigation_id).first()
    db.close()

    if not investigation:
        raise HTTPException(status_code=404, detail="Investigación no encontrada")

    return {
        "id": investigation.id,
        "topic": investigation.topic,
        "internal_sections": investigation.internal_sections,
        "filename": investigation.filename,
        "paragraphs": investigation.paragraphs,
        "citations_count": investigation.citations_count,
        "created_at": investigation.created_at
    }

@router.get("/investigations/search")
async def search_investigations_by_topic(topic: str = Query(..., description="Tema a buscar dentro de las investigaciones")):
    db = SessionLocal()
    investigations = db.query(Investigation).filter(Investigation.topic.ilike(f"%{topic}%")).all()
    db.close()

    return [
        {
            "id": inv.id,
            "topic": inv.topic,
            "internal_sections": inv.internal_sections,
            "filename": inv.filename,
            "paragraphs": inv.paragraphs,
            "citations_count": inv.citations_count,
            "created_at": inv.created_at
        }
        for inv in investigations
    ]