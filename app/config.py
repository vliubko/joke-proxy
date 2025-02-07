import os
from dotenv import load_dotenv

load_dotenv()

# construct MONGO_URI from environment variables
DB_NAME = os.getenv("DB_NAME", "jokesDB")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "example")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "27017")
MONGO_URI = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# get other environment variables
JOKE_API_URL = os.getenv("JOKE_API_URL", "https://v2.jokeapi.dev/joke/Any?contains=")
