from api.settings import DB_URL
from sqlalchemy import create_engine
from api.models.quiz import Base as Quiz

engine = create_engine(DB_URL, echo=True)

def reset_database():
    Quiz.metadata.drop_all(bind=engine)
    Quiz.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()