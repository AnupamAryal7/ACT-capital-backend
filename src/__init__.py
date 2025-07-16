from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import initdb

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb()
    yield
    print("server is stopping")
