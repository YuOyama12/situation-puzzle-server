from api.models.quiz import Quiz
from api.models.user import User
from api.settings import DB_URL
from sqlalchemy import create_engine
from data.database.db import Base

engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()