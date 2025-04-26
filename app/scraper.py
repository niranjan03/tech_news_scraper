import feedparser
from datetime import datetime
from app.database_operations import add_news_item
from config import Config

class NewsScraper:
    def scrape_all(self):
        for source, url in Config.NEWS_SOURCES.items():
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                news_item = {
                    'source': source,
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.get('published'),
                    'summary': entry.get('summary'),
                    'scraped_at': datetime.utcnow().isoformat()
                }
                if add_news_item(news_item):
                    print(f"✅ Added: {entry.title[:50]}...")
                else:
                    print(f"⏩ Skipped duplicate: {entry.title[:50]}...")