# AI News Aggregator

Automatisches System zur Aggregation und Filterung von KI-relevanten News aus verschiedenen RSS-Feeds mit geplanter PDF- und Audio-Export-Funktionalität.

## Projektziel

Tägliche Sammlung relevanter KI-News aus mehreren Quellen mit intelligenter Filterung und Aufbereitung als strukturierter Report (PDF und optional Audio).

## Aktuelle Features

- Multi-Source RSS Aggregation aus 7 verschiedenen Feeds
- Keyword-basierte Filterung nach definierten Themenbereichen
- HTML-Tag-Entfernung aus Artikel-Zusammenfassungen
- Sprachfilterung (Englisch/Deutsch)
- Chronologische Sortierung (neueste zuerst)
- Limitierung auf Top-20-Artikel

## Quellen

- VentureBeat AI
- TechCrunch AI
- The Verge AI
- Hugging Face Blog
- Dev.to AI Tag
- Hacker News (gefiltert nach LLM/Agent/Ollama)
- ArXiv Computer Science AI

## Projektstruktur
```
ai_news_aggregator/
├── src/
│   ├── rss_collector.py       # Hauptskript für RSS-Feed Collection
│   ├── processors/
│   │   ├── filter.py           # Keyword-Filterung
│   │   └── language_filter.py  # Sprachfilterung
│   └── exporters/              # geplant für PDF/Audio Export
├── data/
│   ├── raw/                    # Rohdaten
│   ├── processed/              # Verarbeitete Daten
│   └── output/                 # Finale Outputs
├── requirements.txt
├── .env
└── .gitignore
```

## Installation

### Voraussetzungen
- Python 3.8 oder höher
- pip Package Manager

### Setup

1. Repository klonen
```bash
git clone https://github.com/Voidelele/ai-news-aggregator.git
cd ai-news-aggregator
```

2. Virtual Environment erstellen und aktivieren
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

3. Dependencies installieren
```bash
pip install -r requirements.txt
```

4. Ausführen
```bash
python src/rss_collector.py
```

## Entwicklungs-Roadmap

### Phase 1: Foundation (Abgeschlossen)
- RSS-Feed Collector mit Multi-Source Support
- Keyword-basierte Filterung
- HTML-Bereinigung
- Sprachfilter
- Sortierung und Limitierung

### Phase 2: PDF-Export (Nächster Schritt)
- ReportLab oder FPDF2 Integration
- Layout-Design mit Header, Footer und Sections
- Automatische PDF-Generierung
- Kategorisierung nach Themenbereichen

### Phase 3: Audio-Export (Geplant)
- Text-to-Speech Integration
- Intro/Outro-Erstellung
- MP3-Export mit Metadaten
- Optimierung für 15-20 Minuten Länge

### Phase 4: Erweiterung & Automatisierung (Geplant)
- Task Scheduler / Cron-Job Integration
- NewsAPI Integration
- Reddit API Integration
- Optional: Lokale LLM-Zusammenfassungen via Ollama
- Email-Versand des Reports

## Konfiguration

### Filter-Keywords

Das System filtert nach folgenden Themenbereichen:

**Lokale LLMs**: Ollama, LM Studio, llama.cpp, GPT4All, LocalAI

**Agents & Automation**: LangChain, CrewAI, AutoGPT, n8n, Claude Computer Use

**RAG**: Retrieval Augmented Generation, Vector Databases, Embeddings

**Fine-Tuning**: LoRA, QLoRA, Model Training

**Tools**: Cursor, Windsurf, Coding Assistants

## Tech Stack

- Python 3.13
- feedparser (RSS-Feed Parsing)
- BeautifulSoup4 (HTML Processing)
- python-dateutil (Date Handling)
- reportlab (geplant)
- pyttsx3 (geplant)

## Development Log

**23.02.2026**
- Projektstruktur initialisiert
- RSS Collector implementiert
- Filter-System entwickelt
- Version Control Setup

## Status

Phase 1 abgeschlossen. Phase 2 (PDF-Export) in Vorbereitung.