import pytest
import uuid
from pages.projects_page import ProjectsPage


class TestProjects:
    @pytest.fixture
    def projects_page(self):
        return ProjectsPage()

    @pytest.fixture
    def project_data(self):
        """Фикстура с базовыми данными проекта"""
        return {
            "title": f"Test Project {uuid.uuid4().hex[:8]}",
            "description": "Test project description"
        }

    @pytest.fixture
    def created_project(self, projects_page, project_data):
        """Фикстура для создания проекта и его последующего удаления"""
        response = projects_page.create_project(project_data)
        assert response.status_code == 201
        project_id = response.json()["id"]
        
        yield project_id
        
        # Очистка после теста
        projects_page.delete_project(project_id)

    # POSITIVE TESTS

    def test_create_project_positive(self, projects_page, project_data):
        """Позитивный тест создания проекта"""
        response = projects_page.create_project(project_data)
        
        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["title"] == project_data["title"]
        assert response.json()["description"] == project_data["description"]
        
        # Очистка
        projects_page.delete_project(response.json()["id"])

    def test_get_project_positive(self, projects_page, created_project):
        """Позитивный тест получения проекта"""
        response = projects_page.get_project(created_project)
        
        assert response.status_code == 200
        assert response.json()["id"] == created_project
        assert "title" in response.json()
        assert "description" in response.json()

    def test_update_project_positive(self, projects_page, created_project):
        """Позитивный тест обновления проекта"""
        update_data = {
            "title": f"Updated Project {uuid.uuid4().hex[:8]}",
            "description": "Updated description"
        }
        
        response = projects_page.update_project(created_project, update_data)
        
        assert response.status_code == 204
        
        # Проверяем, что данные обновились
        get_response = projects_page.get_project(created_project)
        assert get_response.json()["title"] == update_data["title"]
        assert get_response.json()["description"] == update_data["description"]

    # NEGATIVE TESTS

    def test_create_project_negative_missing_title(self, projects_page):
        """Негативный тест создания проекта без обязательного поля title"""
        invalid_data = {
            "description": "Project without title"
        }
        
        response = projects_page.create_project(invalid_data)
        
        assert response.status_code == 400

    def test_create_project_negative_empty_data(self, projects_page):
        """Негативный тест создания проекта с пустыми данными"""
        response = projects_page.create_project({})
        
        assert response.status_code == 400

    def test_get_project_negative_invalid_id(self, projects_page):
        """Негативный тест получения проекта с несуществующим ID"""
        invalid_id = "invalid-project-id"
        response = projects_page.get_project(invalid_id)
        
        assert response.status_code == 404

    def test_update_project_negative_invalid_id(self, projects_page):
        """Негативный тест обновления проекта с несуществующим ID"""
        update_data = {"title": "Updated Title"}
        invalid_id = "invalid-project-id"
        
        response = projects_page.update_project(invalid_id, update_data)
        
        assert response.status_code == 404

    def test_update_project_negative_empty_data(self, projects_page, created_project):
        """Негативный тест обновления проекта с пустыми данными"""
        response = projects_page.update_project(created_project, {})
        
        assert response.status_code == 400

    def test_update_project_negative_invalid_data_type(self, projects_page, created_project):
        """Негативный тест обновления проекта с неверным типом данных"""
        invalid_data = {
            "title": 12345,  # Число вместо строки
            "description": True  # Boolean вместо строки
        }
        
        response = projects_page.update_project(created_project, invalid_data)
        
        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422]