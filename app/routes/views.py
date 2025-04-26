from flask import render_template, Blueprint
from app.extensions import db
from app.models import TechNews

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    """Display latest news articles"""
    articles = TechNews.query.order_by(TechNews.scraped_at.desc()).limit(20).all()
    return render_template('index.html', articles=articles)

@bp.route('/source/<source_name>')
def by_source(source_name):
    """Display articles by specific source"""
    articles = TechNews.query.filter_by(source=source_name)\
                           .order_by(TechNews.scraped_at.desc())\
                           .limit(50).all()
    return render_template('source.html', 
                         articles=articles, 
                         source_name=source_name)

@bp.route('/latest')
def latest():
    """JSON endpoint for latest articles"""
    articles = TechNews.query.order_by(TechNews.scraped_at.desc()).limit(10).all()
    return {'articles': [article.to_dict() for article in articles]}