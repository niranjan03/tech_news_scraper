import time
import logging
from datetime import datetime
from app.services.scraper import NewsScraper
from app.extensions import db
from app import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

def run_scraper():
    app = create_app()
    with app.app_context():
        try:
            start_time = datetime.now()
            logging.info(f"🚀 Starting scraping at {start_time}")
            
            NewsScraper.scrape_all()
            
            duration = (datetime.now() - start_time).total_seconds()
            logging.info(f"✅ Completed in {duration:.2f} seconds")
            logging.info("🗞️ Articles scraped and saved to the database")
            logging.info("🔄 Committing changes to the database")
            db.session.commit()

        except Exception as e:
            logging.error(f"🔥 Scraping failed: {str(e)}")
            db.session.rollback()

if __name__ == "__main__":
    while True:
        run_scraper()
        logging.info("⏳ Next run in 10 minutes...")
        time.sleep(600)  # 10 minutes