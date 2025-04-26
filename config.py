import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    # Get absolute path to CA certificate
    ca_path = Path(__file__).parent / 'ca.pem'
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'sslmode': 'require',
            'sslrootcert': str(ca_path),
            'connect_timeout': 5
        }
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    NEWS_SOURCES = {
        "TechCrunch": "https://techcrunch.com/feed/",
    "TheVerge": "https://www.theverge.com/rss/index.xml",
    "Wired": "https://www.wired.com/feed/rss",
    "HackerNews": "https://news.ycombinator.com/rss",
    "ArsTechnica": "http://feeds.arstechnica.com/arstechnica/index",
    "ArsTechnica": "https://www.bloomberg.com/technology",
    "ArsTechnica":"https://www.cnbc.com/id/19700125/device/rss/rss.html",
    "ArsTechnica":"https://www.forbes.com/technology/feed/",
    "ArsTechnica":"https://www.engadget.com/rss.xml",
    "ArsTechnica":"https://www.recode.net/rss/index.xml",
    "ArsTechnica":"https://www.zdnet.com/news/rss.xml",
    "ArsTechnica":"https://www.theinformation.com/rss",
    "ArsTechnica":"https://www.businessinsider.com/rss",
    "ArsTechnica":"https://www.theguardian.com/technology/rss",
    "ArsTechnica":"https://www.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "ArsTechnica":"https://www.bbc.co.uk/news/technology/rss.xml",
    }