from datetime import datetime
import random
from app.models.response_model import Citation

def generate_fake_citation(topic: str, max_age: int, existing_citations: set) -> Citation:
    current_year = datetime.now().year
    oldest_year = current_year - max_age

    authors = [
        "Smith J.", "Doe A.", "Brown B.", "Taylor C.", "Wilson D.",
        "Anderson E.", "Clark F.", "Lopez G.", "Nguyen H.", "Patel K."
    ]

    journals = [
        "Journal of Medical Studies",
        "International Review of Science",
        "Health and Research",
        "Clinical Updates",
        "Scientific Advances Journal",
        "Annals of Experimental Medicine",
        "Global Health Perspectives",
        "Frontiers in Biomedical Research"
    ]

    # Nuevos títulos variados
    title_templates = [
        f"Advances in {topic}: A Comprehensive Review",
        f"The Impact of {topic} on Modern Science",
        f"Recent Developments Regarding {topic}",
        f"Exploring the Complexities of {topic}",
        f"New Frontiers in {topic} Research",
        f"Applications and Innovations in {topic}",
        f"The Role of {topic} in Contemporary Medicine",
        f"Emerging Trends in {topic}",
        f"{topic}: Challenges and Opportunities",
        f"Critical Perspectives on {topic}"
    ]

    while True:
        random_year = random.randint(oldest_year, current_year)
        author = random.choice(authors)
        title = random.choice(title_templates)
        journal = random.choice(journals)
        doi = f"https://doi.org/10.{random.randint(1000,9999)}/{random.randint(10000,99999)}"

        citation_key = (author, random_year, title, journal)

        if citation_key not in existing_citations:
            existing_citations.add(citation_key)
            break

    return Citation(
        author=author,
        year=random_year,
        title=title,
        journal=journal,
        doi_or_url=doi,
        access_date=datetime.now().strftime("%Y-%m-%d")
    )