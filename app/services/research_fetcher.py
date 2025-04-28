import requests
from scholarly import scholarly
from pymed import PubMed

# Función para buscar en PubMed
def search_pubmed(topic, max_results=5):
    pubmed = PubMed()
    results = pubmed.query(topic, max_results=max_results)
    articles = []
    for article in results:
        articles.append({
            "title": article.title,
            "journal": article.journal,
            "year": article.publication_date.year if article.publication_date else "No disponible",
            "authors": [a['lastname'] for a in article.authors] if article.authors else [],
            "doi": article.doi
        })
    return articles

# Función para buscar en Google Scholar
def search_google_scholar(topic, max_results=5):
    search_query = scholarly.search_pubs(topic)
    articles = []
    for _ in range(max_results):
        try:
            result = next(search_query)
            articles.append({
                "title": result.get('bib', {}).get('title'),
                "journal": result.get('bib', {}).get('venue'),
                "year": result.get('bib', {}).get('pub_year'),
                "authors": result.get('bib', {}).get('author', "").split(' and '),
                "doi": None  # Google Scholar no da DOI directamente
            })
        except StopIteration:
            break
    return articles

# Función para buscar en Crossref
def search_crossref(topic, max_results=5):
    url = f"https://api.crossref.org/works?query={topic}&rows={max_results}"
    response = requests.get(url)
    articles = []
    if response.status_code == 200:
        data = response.json()
        for item in data.get('message', {}).get('items', []):
            articles.append({
                "title": item.get('title', [""])[0],
                "journal": item.get('container-title', [""])[0] if item.get('container-title') else None,
                "year": item.get('issued', {}).get('date-parts', [[None]])[0][0],
                "authors": [author.get('family') for author in item.get('author', []) if 'family' in author],
                "doi": item.get('DOI')
            })
    return articles

# Función general para combinar todas las fuentes
def fetch_research_sources(topic, max_results=5):
    results = []
    results.extend(search_pubmed(topic, max_results))
    results.extend(search_google_scholar(topic, max_results))
    results.extend(search_crossref(topic, max_results))
    return results