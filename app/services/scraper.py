import feedparser
from datetime import datetime
from app.services.database import execute_query
from config import Config

class NewsScraper:
    @staticmethod
    def scrape_all():
        for source, url in Config.NEWS_SOURCES.items():
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                NewsScraper.process_entry(source, entry)
    
    @staticmethod
    def process_entry(source, entry):
        query = """
        INSERT INTO tech_news 
        (source, title, link, published, summary, scraped_at)
        VALUES (:source, :title, :link, :published, :summary, :scraped_at)
        ON CONFLICT (link) DO UPDATE SET 
            is_new = EXCLUDED.link != tech_news.link
        """
        
        params = {
            'source': source,
            'title': entry.title,
            'link': entry.link,
            'published': entry.get('published'),
            'summary': entry.get('summary'),
            'scraped_at': datetime.utcnow().isoformat()
        }
        
        execute_query(query, params)