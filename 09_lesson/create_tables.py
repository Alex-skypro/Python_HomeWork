from database.models import Base
from database.session import engine

def create_tables():
    """Создание таблиц в БД"""
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()