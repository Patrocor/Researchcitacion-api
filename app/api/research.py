from fastapi import APIRouter
from app.models.request_model import ResearchRequest
from app.services.document_generator import generate_docx
from app.services.research_fetcher import fetch_research_sources

router = APIRouter(prefix="/api", tags=["Research"])

@router.post("/generate-research")
async def generate_research(request: ResearchRequest):
    # Buscar artículos reales
    citations = fetch_research_sources(request.topic, max_results=5)

    # Crear secciones basadas en las partes internas que pide el usuario
    sections = []
    for section in request.internal_sections:
        paragraphs = []
        for _ in range(request.paragraphs):
            paragraph_text = f"Contenido generado sobre {section} relacionado a {request.topic}."
            paragraphs.append({
                "text": paragraph_text,
                "citations": citations
            })
        sections.append({
            "title": section,
            "paragraphs": paragraphs
        })

    # Generar el archivo Word real basado en las citas reales obtenidas
    return generate_docx(sections, citations, request.topic)