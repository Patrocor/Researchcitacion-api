from sqlalchemy.orm import Session
from app.database.models import Investigation
import json

def create_investigation(db: Session, topic: str, internal_sections: list, filename: str, paragraphs: int, citations_count: int):
    sections_text = json.dumps(internal_sections) if internal_sections else ""
    
    db_investigation = Investigation(
        topic=topic,
        internal_sections=sections_text,
        filename=filename,
        paragraphs=paragraphs,
        citations_count=citations_count
    )
    db.add(db_investigation)
    db.commit()
    db.refresh(db_investigation)
    return db_investigation