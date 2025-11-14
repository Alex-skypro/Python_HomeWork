import pytest
import time
import random
import string
from api.yougile_api import YougileAPI


class TestYougileProjects:
    
    def generate_unique_name(self, prefix="TestProject"):
        """Генерация уникального имени для проекта"""
        timestamp = int(time.time())
        random_suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
        return f"{prefix}_{timestamp}_{random_suffix}"
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = YougileAPI()
        self.created_projects = []
        yield
        self.cleanup_projects()
    
    def cleanup_projects(self):
        """Очистка созданных проектов после тестов"""
        for project_id in self.created_projects:
            try:
                self.api.delete_project(project_id)
            except:
                pass  # Игнорируем ошибки при удалении
    
    # POSITIVE TESTS
    
    def test_create_project_positive(self):
        """Позитивный тест создания проекта"""
        project_data = {
            "title": self.generate_unique_name("Positive"),
            "description": "Test description for positive case"
        }
        
        response = self.api.create_project(project_data)
        
        # Yougile может возвращать 200 вместо 201
        assert response.status_code in [200, 201], f"Expected 200 or 201, got {response.status_code}. Response: {response.text}"
        
        response_data = response.json()
        assert "id" in response_data
        assert response_data["title"] == project_data["title"]
        
        project_id = response_data["id"]
        self.created_projects.append(project_id)
    
    def test_get_project_positive(self):
        """Позитивный тест получения проекта"""
        # Сначала создаем проект
        project_data = {
            "title": self.generate_unique_name("GetTest"),
            "description": "Project for get testing"
        }
        create_response = self.api.create_project(project_data)
        assert create_response.status_code in [200, 201]
        
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)
        
        # Получаем проект
        response = self.api.get_project(project_id)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
        response_data = response.json()
        assert response_data["id"] == project_id
        assert response_data["title"] == project_data["title"]
    
    def test_update_project_positive(self):
        """Позитивный тест обновления проекта"""
        # Сначала создаем проект
        project_data = {
            "title": self.generate_unique_name("UpdateTest"),
            "description": "Original description"
        }
        create_response = self.api.create_project(project_data)
        assert create_response.status_code in [200, 201]
        
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)
        
        # Обновляем проект
        update_data = {
            "title": self.generate_unique_name("Updated"),
            "description": "Updated description"
        }
        response = self.api.update_project(project_id, update_data)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
        response_data = response.json()
        assert response_data["title"] == update_data["title"]
        assert response_data["description"] == update_data["description"]
    
    # NEGATIVE TESTS
    
    def test_create_project_negative_empty_title(self):
        """Негативный тест создания проекта с пустым title"""
        project_data = {
            "title": "",  # Пустой title
            "description": "Project with empty title"
        }
        
        response = self.api.create_project(project_data)
        
        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422], f"Expected 400 or 422, got {response.status_code}. Response: {response.text}"
    
    def test_create_project_negative_missing_title(self):
        """Негативный тест создания проекта без title"""
        project_data = {
            "description": "Project without title"  # Нет поля title
        }
        
        response = self.api.create_project(project_data)
        
        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422], f"Expected 400 or 422, got {response.status_code}. Response: {response.text}"
    
    def test_get_project_negative_not_found(self):
        """Негативный тест получения несуществующего проекта"""
        # Генерируем случайный ID, который точно не существует
        non_existent_id = "nonexistent123456789"
        
        response = self.api.get_project(non_existent_id)
        
        # Yougile может возвращать 404 или 400 для невалидного ID
        assert response.status_code in [400, 404], f"Expected 400 or 404, got {response.status_code}. Response: {response.text}"
    
    def test_update_project_negative_not_found(self):
        """Негативный тест обновления несуществующего проекта"""
        non_existent_id = "nonexistent123456789"
        update_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }
        
        response = self.api.update_project(non_existent_id, update_data)
        
        # Ожидаем ошибку
        assert response.status_code in [400, 404], f"Expected 400 or 404, got {response.status_code}. Response: {response.text}"
    
    def test_update_project_negative_empty_title(self):
        """Негативный тест обновления проекта с пустым title"""
        # Сначала создаем проект
        project_data = {
            "title": self.generate_unique_name("InvalidUpdate"),
            "description": "Original description"
        }
        create_response = self.api.create_project(project_data)
        assert create_response.status_code in [200, 201]
        
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)
        
        # Пытаемся обновить с пустым title
        invalid_data = {
            "title": "",  # Пустой title недопустим
            "description": "Updated description"
        }
        
        response = self.api.update_project(project_id, invalid_data)
        
        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422], f"Expected 400 or 422, got {response.status_code}. Response: {response.text}"