import random
from app.services.translator import translate_to_spanish
from app.services.citation_generator import generate_fake_citation
from app.models.response_model import Paragraph

def generate_fake_paragraph(topic: str, max_age: int, num_citations: int, existing_citations: set) -> Paragraph:
    intro_phrases_en = [
        f"Recent studies on {topic} have provided new insights into its mechanisms.",
        f"The field of {topic} has undergone significant developments in recent years.",
        f"Emerging research on {topic} suggests new avenues for exploration.",
        f"Scientific investigations have expanded our understanding of {topic}.",
        f"An increased interest in {topic} has led to groundbreaking discoveries."
    ]

    body_phrases_en = [
        f"These findings highlight the importance of continued research in {topic}.",
        f"Results indicate a complex interplay of factors influencing {topic}.",
        f"Experts recommend further studies to validate the recent observations regarding {topic}.",
        f"Understanding {topic} is crucial for future applications in various fields.",
        f"Preliminary evidence underscores a promising future for therapies based on {topic}."
    ]

    conclusion_phrases_en = [
        f"Continued exploration of {topic} may yield significant scientific and clinical advancements.",
        f"Future research is needed to confirm and expand on these promising results about {topic}.",
        f"The evolving knowledge of {topic} will likely impact multiple disciplines.",
        f"Researchers anticipate that breakthroughs in {topic} will transform current practices.",
        f"The growing body of evidence about {topic} opens exciting possibilities for innovation."
    ]

    intro = random.choice(intro_phrases_en)
    body = random.choice(body_phrases_en)
    conclusion = random.choice(conclusion_phrases_en)

    paragraph_text = f"{intro} {body} {conclusion}"

    translated_paragraph = translate_to_spanish(paragraph_text)

    citations = [generate_fake_citation(topic, max_age, existing_citations) for _ in range(num_citations)]

    return Paragraph(
        text=translated_paragraph,
        citations=citations
    )