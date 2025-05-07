# Tech News Scraper

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Flask](https://img.shields.io/badge/flask-2.0+-green)

Scrapes technology news from multiple sources and stores in PostgreSQL.

## Features
- Scrapes 10+ tech news sites
- Stores in AWS RDS PostgreSQL
- CI/CD pipeline with GitHub Actions
- Docker support

## Setup
```bash
git clone https://github.com/yourusername/tech-news-scraper.git
cd tech-news-scraper
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt