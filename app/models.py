from datetime import datetime
from app.extensions import db

class TechNews(db.Model):
    __tablename__ = 'tech_news'
    
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(300), nullable=False, index=True)
    link = db.Column(db.String(300), nullable=False, unique=True)
    published = db.Column(db.DateTime, index=True)
    summary = db.Column(db.Text)
    scraped_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_new = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'source': self.source,
            'title': self.title,
            'link': self.link,
            'published': self.published.isoformat() if self.published else None,
            'summary': self.summary,
            'scraped_at': self.scraped_at.isoformat()
        }