from sqlalchemy import text
from app import create_app, db

def add_news_item(item):
    app = create_app()
    with app.app_context():
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("""
                    INSERT INTO tech_news 
                    (source, title, link, published, summary, scraped_at)
                    VALUES (:source, :title, :link, :published, :summary, :scraped_at)
                    ON CONFLICT (link) DO NOTHING
                    RETURNING id
                    """),
                    item
                )
                connection.commit()
                return result.scalar()
        except Exception as e:
            print(f"Database error: {str(e)}")
            return None