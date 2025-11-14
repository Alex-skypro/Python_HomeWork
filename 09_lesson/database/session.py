from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# Создаем движок и сессию
engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    """Генератор сессии для зависимостей"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        