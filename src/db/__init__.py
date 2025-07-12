from fastapi import FastAPI
from contextlib import asynccontextmanager

# add lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("the server is running...")
    yield
    print("the server is stopped.")

app = FastAPI(lifespan=lifespan)