FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

# Install Poetry for dependency management
RUN pip install poetry

# Install dependencies with Poetry
RUN poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY app/ ./app/

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
