import requests
from config import Config


class YougileAPI:
    def __init__(self):
        self.base_url = f"{Config.BASE_URL}/{Config.API_VERSION}"
        self.auth = (Config.API_USER, Config.API_TOKEN)  # Yougile использует Basic auth
    
    def create_project(self, data):
        """POST /api-v2/projects - создание проекта"""
        response = requests.post(
            f"{self.base_url}/projects",
            auth=self.auth,
            json=data
        )
        return response
    
    def get_project(self, project_id):
        """GET /api-v2/projects/{id} - получение проекта"""
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            auth=self.auth
        )
        return response
    
    def update_project(self, project_id, data):
        """PUT /api-v2/projects/{id} - обновление проекта"""
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            auth=self.auth,
            json=data
        )
        return response
    
    def delete_project(self, project_id):
        """DELETE /api-v2/projects/{id} - удаление проекта (для очистки)"""
        response = requests.delete(
            f"{self.base_url}/projects/{project_id}",
            auth=self.auth
        )
        return response