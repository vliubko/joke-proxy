from fastapi import FastAPI, HTTPException
from app.api import get_joke
from app.database import save_joke, check_db_connection
from app.logging import setup_logging

# Setup logging
logger = setup_logging()

app = FastAPI(docs_url="/")  # Moves Swagger UI to root "/"

@app.get("/health")
async def health_check():
    logger.info("Health check requested")
    try:
        result = check_db_connection()
        return {"status": "healthy", "database": "connected", "ping": result}
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Database connection failed")

@app.get("/joke/{query}")
async def search_joke(query: str):
    logger.info(f"Received request for joke with query: {query}")
    joke = get_joke(query)
    if joke:
        logger.info(f"Joke found: {joke}")
        save_joke(joke)  # Save joke to DB
    else:
        logger.warning(f"No joke found for query: {query}")
    return {"joke": joke or "No jokes found!"}
