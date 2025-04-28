import random
from app.models.response_model import Citation

def simulate_quality_check(citations: list[Citation]) -> list[dict]:
    """
    Simula un control de calidad sobre las citas generadas.
    De forma aleatoria, puede marcar una cita como 'Retracted'.
    """
    quality_issues = []

    if citations:
        # 30% de probabilidad de encontrar un problema en una cita
        if random.random() < 0.3:
            problematic_citation = random.choice(citations)
            issue_detail = {
                "citation": f"{problematic_citation.author} ({problematic_citation.year}). {problematic_citation.title}. {problematic_citation.journal}. {problematic_citation.doi_or_url}",
                "issue": "Retracted paper detected"
            }
            quality_issues.append(issue_detail)

    return quality_issues