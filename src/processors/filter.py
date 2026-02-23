def filter_by_keywords(articles: list[dict], keywords: list[str]) -> list[dict]:
    """
    Filtert Artikel nach Keywords in Titel und Summary.
    
    Args:
        articles: Liste von Artikel-Dictionaries
        keywords: Liste von Keywords zum Suchen
        
    Returns:
        Gefilterte Liste von Artikeln die mindestens ein Keyword enthalten
    """
    filtered = []
    
    for article in articles:
        # Titel und Summary in Kleinbuchstaben für case-insensitive Suche
        title_lower = article["title"].lower()
        summary_lower = article["summary"].lower()
        
        # Prüfe ob irgendein Keyword vorkommt
        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in title_lower or keyword_lower in summary_lower:
                filtered.append(article)
                break  # Artikel gefunden, kein weiteres Keyword prüfen
    
    return filtered