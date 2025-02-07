import requests
from app.config import JOKE_API_URL

def get_joke(query: str) -> str:
    response = requests.get(f"{JOKE_API_URL}{query}")
    if response.status_code == 200:
        data = response.json()
        if data.get("joke"):
            return data["joke"]
        elif "setup" in data and "delivery" in data:
            return f"{data['setup']} - {data['delivery']}"
    return None
