from flask import Blueprint, jsonify
from app.extensions import db
from app.models import TechNews
from flask import request

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/news')
def get_all_news():
    """Get all news articles (paginated)"""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 20, type=int), 100)
    pagination = TechNews.query.order_by(TechNews.scraped_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'articles': [article.to_dict() for article in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    })

@bp.route('/news/<int:article_id>')
def get_article(article_id):
    """Get single article by ID"""
    article = TechNews.query.get_or_404(article_id)
    return jsonify(article.to_dict())

@bp.route('/sources')
def get_sources():
    """Get list of all news sources"""
    sources = db.session.query(TechNews.source.distinct()).all()
    return jsonify({'sources': [s[0] for s in sources]})

@bp.route('/search')
def search():
    """Search articles by keyword"""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Missing search query'}), 400
    
    results = TechNews.query.filter(
        TechNews.title.ilike(f'%{query}%') | 
        TechNews.summary.ilike(f'%{query}%')
    ).order_by(TechNews.scraped_at.desc()).limit(50).all()
    
    return jsonify({'results': [article.to_dict() for article in results]})