from pydantic import BaseModel
from typing import List, Optional

class Citation(BaseModel):
    author: Optional[str]
    year: Optional[int]
    title: Optional[str]
    journal: Optional[str]
    doi_or_url: Optional[str]
    access_date: Optional[str]

class Paragraph(BaseModel):
    text: str
    citations: List[Citation]

class ResearchResponse(BaseModel):
    status: str
    citation_style: str
    paragraphs: List[Paragraph]
    references: List[dict]
    quality_assurance: dict