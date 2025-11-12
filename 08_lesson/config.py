class Config:
    BASE_URL = "https://yougile.com/api-v2"
    # Для наставника: необходимо добавить ваш API токен ниже
    API_TOKEN = "YOUR_API_TOKEN_HERE"
    
    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }