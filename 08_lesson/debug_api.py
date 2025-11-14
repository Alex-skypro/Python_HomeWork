from api.yougile_api import YougileAPI
from config import Config

def debug_auth():
    """Проверка авторизации"""
    api = YougileAPI()
    
    print("=== Debug Auth ===")
    print(f"Base URL: {api.base_url}")
    print(f"Auth: {api.auth}")
    
    # Пробуем получить список проектов
    response = api.get_projects_list()
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text[:200]}...")

if __name__ == "__main__":
    debug_auth()