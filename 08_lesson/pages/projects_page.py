import requests
from config import Config


class ProjectsPage:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS

    def create_project(self, project_data):
        """POST /api-v2/projects - Создание проекта"""
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=project_data, headers=self.headers)
        return response

    def get_project(self, project_id):
        """GET /api-v2/projects/{id} - Получение проекта по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, update_data):
        """PUT /api-v2/projects/{id} - Обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=update_data, headers=self.headers)
        return response

    def delete_project(self, project_id):
        """DELETE /api-v2/projects/{id} - Удаление проекта (для очистки)"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        return response