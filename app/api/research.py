from fastapi import APIRouter
from app.models.request_model import ResearchRequest
from app.models.response_model import ResearchResponse
from app.services.document_generator import generate_docx
from app.database.db import SessionLocal
from app.database.crud import create_investigation

router = APIRouter(prefix="/api", tags=["Research Generator"])

@router.post("/generate-research", response_model=None)
async def generate_research(request: ResearchRequest):
    sections = []

    if request.internal_sections:
        for section_title in request.internal_sections:
            paragraphs = [
                {
                    "text": f"Texto desarrollado para {section_title}",
                    "citations": [
                        {
                            "author": "Autor Ejemplo",
                            "year": 2024,
                            "title": f"Estudio sobre {section_title}",
                            "journal": "Journal of Advanced Studies",
                            "doi_or_url": "https://doi.org/10.1234/example",
                            "access_date": "2025-04-27"
                        }
                    ]
                }
                for _ in range(request.paragraphs)
            ]
            sections.append({
                "section_title": section_title,
                "paragraphs": paragraphs
            })
    else:
        paragraphs = [
            {
                "text": f"Texto desarrollado para {request.topic}",
                "citations": [
                    {
                        "author": "Autor Ejemplo",
                        "year": 2024,
                        "title": f"Estudio sobre {request.topic}",
                        "journal": "Journal of Advanced Studies",
                        "doi_or_url": "https://doi.org/10.1234/example",
                        "access_date": "2025-04-27"
                    }
                ]
            }
            for _ in range(request.paragraphs)
        ]
        sections.append({
            "section_title": request.topic,
            "paragraphs": paragraphs
        })

    all_citations = [c for sec in sections for p in sec["paragraphs"] for c in p["citations"]]

    references = [
        {"reference_text": f"{c['author']} ({c['year']}). {c['title']}. {c['journal']}. {c['doi_or_url']}"}
        for c in all_citations
    ]

    filename = f"investigacion_{request.topic.replace(' ', '_')}.docx"

    # Guardar en la base de datos
    db = SessionLocal()
    create_investigation(
        db=db,
        topic=request.topic,
        internal_sections=request.internal_sections,
        filename=filename,
        paragraphs=len(sections),
        citations_count=len(all_citations)
    )
    db.close()

    return generate_docx(sections, references, request.topic)