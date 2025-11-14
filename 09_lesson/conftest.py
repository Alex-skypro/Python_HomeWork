import pytest
import random
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Student
from config import Config
from database.session import SessionLocal, get_db_session


@pytest.fixture(scope="function")
def db_session():
    """Фикстура для сессии БД с автоматической очисткой"""
    session = SessionLocal()
    
    # Включаем режим тестирования
    session.begin_nested()
    
    yield session
    
    # Откатываем изменения после теста
    session.rollback()
    session.close()


@pytest.fixture
def test_student_data():
    """Генератор тестовых данных для студента"""
    def _generate_data(prefix="test"):
        random_suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
        return {
            "name": f"{prefix}_student_{random_suffix}",
            "email": f"{prefix}.student.{random_suffix}@test.com",
            "age": random.randint(18, 25)
        }
    return _generate_data


@pytest.fixture
def cleanup_test_data(db_session):
    """Фикстура для очистки тестовых данных"""
    test_emails = []
    
    def _mark_for_cleanup(email):
        test_emails.append(email)
    
    yield _mark_for_cleanup
    
    # Очищаем тестовые данные после выполнения теста
    for email in test_emails:
        try:
            # Hard delete для тестовых данных
            db_session.query(Student).filter(Student.email == email).delete()
            db_session.commit()
        except:
            db_session.rollback()