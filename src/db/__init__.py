from fastapi import FastAPI
from src.reviews.routes import review_route
from contextlib import asynccontextmanager
from src.db.main import initdb

# add lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb()
    yield
    print("the server is stopped.")

app = FastAPI(lifespan=lifespan)

app.include_router(
    review_route,
    prefix="/reviews",
    tags=['review']
)
