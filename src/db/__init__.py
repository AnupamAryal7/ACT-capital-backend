from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import initdb

# add lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb()
    yield
    print("the server is stopped.")

app = FastAPI(lifespan=lifespan)