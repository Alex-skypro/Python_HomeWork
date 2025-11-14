import pytest
from sqlalchemy import func
from database.models import Student
from database.session import get_db_session


class TestStudentsCRUD:
    
    def test_create_student(self, db_session, test_student_data, cleanup_test_data):
        """Тест добавления студента"""
        # Подготовка данных
        student_data = test_student_data("create")
        
        # Создание студента
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        # Помечаем для очистки
        cleanup_test_data(student_data['email'])
        
        # Проверки
        assert new_student.id is not None
        assert new_student.name == student_data['name']
        assert new_student.email == student_data['email']
        assert new_student.age == student_data['age']
        assert new_student.is_deleted is False
        assert new_student.deleted_at is None
        
        # Проверяем, что студент действительно сохранен в БД
        saved_student = db_session.query(Student).filter(Student.id == new_student.id).first()
        assert saved_student is not None
        assert saved_student.email == student_data['email']
    
    def test_update_student(self, db_session, test_student_data, cleanup_test_data):
        """Тест изменения данных студента"""
        # Сначала создаем студента
        student_data = test_student_data("update")
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        cleanup_test_data(student_data['email'])
        
        # Обновляем данные
        updated_name = f"updated_{student_data['name']}"
        updated_age = student_data['age'] + 1
        
        new_student.name = updated_name
        new_student.age = updated_age
        db_session.commit()
        db_session.refresh(new_student)
        
        # Проверяем обновление
        assert new_student.name == updated_name
        assert new_student.age == updated_age
        
        # Проверяем, что обновление сохранилось в БД
        updated_student = db_session.query(Student).filter(Student.id == new_student.id).first()
        assert updated_student.name == updated_name
        assert updated_student.age == updated_age
    
    def test_soft_delete_student(self, db_session, test_student_data, cleanup_test_data):
        """Тест мягкого удаления студента"""
        # Сначала создаем студента
        student_data = test_student_data("delete")
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        cleanup_test_data(student_data['email'])
        
        student_id = new_student.id
        
        # Проверяем, что студент создан и не удален
        initial_student = db_session.query(Student).filter(Student.id == student_id).first()
        assert initial_student.is_deleted is False
        assert initial_student.deleted_at is None
        
        # Выполняем мягкое удаление
        from datetime import datetime
        initial_student.is_deleted = True
        initial_student.deleted_at = datetime.now()
        db_session.commit()
        
        # Проверяем, что студент помечен как удаленный
        deleted_student = db_session.query(Student).filter(Student.id == student_id).first()
        assert deleted_student.is_deleted is True
        assert deleted_student.deleted_at is not None
        
        # Проверяем, что студент не возвращается в обычных запросах
        active_students = db_session.query(Student).filter(Student.is_deleted == False).all()
        student_ids = [s.id for s in active_students]
        assert student_id not in student_ids
    
    def test_hard_delete_student(self, db_session, test_student_data):
        """Тест полного удаления студента (для очистки тестовых данных)"""
        # Создаем студента
        student_data = test_student_data("hard_delete")
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        student_id = new_student.id
        
        # Проверяем, что студент создан
        assert db_session.query(Student).filter(Student.id == student_id).first() is not None
        
        # Выполняем полное удаление
        db_session.query(Student).filter(Student.id == student_id).delete()
        db_session.commit()
        
        # Проверяем, что студент полностью удален из БД
        deleted_student = db_session.query(Student).filter(Student.id == student_id).first()
        assert deleted_student is None
    
    def test_create_student_duplicate_email(self, db_session, test_student_data, cleanup_test_data):
        """Негативный тест: попытка создания студента с дублирующимся email"""
        student_data = test_student_data("duplicate")
        
        # Создаем первого студента
        first_student = Student(**student_data)
        db_session.add(first_student)
        db_session.commit()
        db_session.refresh(first_student)
        
        cleanup_test_data(student_data['email'])
        
        # Пытаемся создать второго студента с тем же email
        second_student_data = student_data.copy()
        second_student = Student(**second_student_data)
        db_session.add(second_student)
        
        # Ожидаем исключение из-за уникальности email
        try:
            db_session.commit()
            # Если commit прошел, это ошибка - тест должен упасть
            assert False, "Expected integrity error for duplicate email"
        except Exception as e:
            # Откатываем сессию
            db_session.rollback()
            # Проверяем, что это ошибка уникальности
            assert "unique" in str(e).lower() or "duplicate" in str(e).lower()