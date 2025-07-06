from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.settings import DB_URL
from data.database.seeders.constants import SAMPLE_QUIZ_ID, SAMPLE_QUIZ_USER_ID
from data.database.tables.favorite import Favorite

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def execute():
    """
    favoritesテーブル内にお気に入りデータを追加する
    """
    session = SessionLocal()

    try:
        favorite = Favorite(
            user_id = SAMPLE_QUIZ_USER_ID,
            quiz_id = SAMPLE_QUIZ_ID,
        )

        session.add(favorite)
        session.flush()
        session.commit()
        print("Inserting favorite data was completed successfully!")    
    except Exception as e:
        print(f"ERROR: {e}")
        session.rollback()
    finally:
        session.close()