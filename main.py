from fastapi import FastAPI
from src.reviews.routes import review_router

version = "v1"

app = FastAPI(
    title="Review overview",
    description="the description",
    version=version
)

app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=['reviews'])