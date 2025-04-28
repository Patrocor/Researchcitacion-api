from pydantic import BaseModel, Field
from typing import List, Optional

class ResearchRequest(BaseModel):
    topic: str = Field(..., description="Topic or subject to investigate.")
    citation_style: str = Field(..., description="Citation style required (e.g., APA 7, Vancouver).")
    max_age: int = Field(..., gt=0, description="Maximum age of the references in years (must be greater than 0).")
    paragraphs: int = Field(..., gt=0, description="Total number of paragraphs requested (must be greater than 0).")
    allowed_sources: List[str] = Field(default=["journals"], description="Allowed sources (e.g., journals, books).")
    internal_sections: Optional[List[str]] = Field(default=None, description="Subtopics or internal sections to organize the research (optional).")