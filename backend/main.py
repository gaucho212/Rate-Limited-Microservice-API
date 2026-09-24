import os
import redis
import psycopg2
from fastapi import FastAPI

app = FastAPI(title="Dockerized Production API")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "app_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

@app.get("/")
def read_root():
    # Licznik odsłon w Redis (Cache/State)
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    hits = r.incr("hits")
    return {"message": "API działa poprawnie!", "odwiedziny_redis": hits}

@app.get("/health")
def health_check():
    # Sprawdzenie połączenia z bazą PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    conn.close()
    return {"status": "healthy", "database": "connected", "redis": "connected"}