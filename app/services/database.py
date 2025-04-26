from sqlalchemy import text
from app.extensions import db
from app import create_app

def execute_query(query, params=None):
    app = create_app()
    with app.app_context():
        try:
            with db.engine.connect() as connection:
                result = connection.execute(text(query), params or {})
                connection.commit()
                return result
        except Exception as e:
            print(f"Database error: {str(e)}")
            raise