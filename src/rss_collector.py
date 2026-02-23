import feedparser
from bs4 import BeautifulSoup
from processors.filter import filter_by_keywords

def html_to_plain_text(html: str, separator: str = " ") -> str:
    
    soup = BeautifulSoup(html,"html.parser")          
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator=separator, strip=True)

def fetch_rss_feed(url:str) -> list[dict]:
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries:
        summary = ""
        if hasattr(entry, 'summary'):
            summary = entry.summary
        elif hasattr(entry, 'description'):
            summary = entry.description
        published = entry.published if hasattr(entry, 'published') else "Kein Datum"
        
        articles.append({
            "title": entry.title, 
            "link": entry.link,
            "summary": html_to_plain_text(summary)[:300] if summary else "Keine Zusammenfassung verfügbar",
            "published": published,
        })
    return articles
def fetch_multiple_feeds(feed_urls: list[str]) -> list[dict]:
    all_articles = []
    
    for url in feed_urls:
        print(f"Fetching: {url}")
        articles = fetch_rss_feed(url)
        all_articles.extend(articles)
    
    return all_articles
def main():
    """Hauptfunktion die den kompletten News-Sammelprozess durchführt."""
    from dateutil import parser as date_parser
    from processors.language_filter import is_latin_script
    
    # Keywords
    keywords = [
        "ollama", "lm studio", "llama.cpp", "gpt4all", "localai",
        "langchain", "crewai", "autogpt", "agent", "n8n",
        "claude", "anthropic", "computer use",
        "rag", "retrieval augmented", "vector database", "embeddings",
        "cursor", "windsurf", "coding assistant",
        "fine-tuning", "lora", "qlora",
    ]
    
    # Feeds
    feed_urls = [
        "https://feeds.feedburner.com/venturebeat/SZYF",
        "https://techcrunch.com/tag/artificial-intelligence/feed/",
        "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "https://huggingface.co/blog/feed.xml",
        "https://dev.to/feed/tag/ai",
        "https://hnrss.org/newest?q=LLM+OR+agent+OR+ollama",
        "http://export.arxiv.org/rss/cs.AI",
    ]
    
    # Artikel sammeln
    print("Sammle Artikel...")
    articles = fetch_multiple_feeds(feed_urls)
    
    # Filtern
    print("Filtere nach Keywords...")
    filtered_articles = filter_by_keywords(articles, keywords)
    
    print("Filtere nach Sprache...")
    latin_articles = [article for article in filtered_articles if is_latin_script(article['title'])]
    
    # Sortieren
    def parse_date_safe(date_str):
        try:
            return date_parser.parse(date_str)
        except:
            return date_parser.parse("1970-01-01")
    
    latin_articles.sort(key=lambda x: parse_date_safe(x['published']), reverse=True)
    
    # Top 20
    top_articles = latin_articles[:20]
    
    # Ausgabe
    print(f"\n{'='*80}")
    print(f"Gefundene Artikel: {len(articles)}")
    print(f"Nach Keywords: {len(filtered_articles)}")
    print(f"Nach Sprache: {len(latin_articles)}")
    print(f"Top Artikel: {len(top_articles)}")
    print(f"{'='*80}\n")
    
    for i, article in enumerate(top_articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   Link: {article['link']}")
        print(f"   Summary: {article['summary']}")
        print(f"   Datum: {article['published']}")
        print()
    
    return top_articles

if __name__ == "__main__":
    articles = main()


        
    