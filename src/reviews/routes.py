from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from src.reviews.review_data import reviews
from src.reviews.schemas import Review

review_router = APIRouter()

@review_router.get('/review', response_model=List[Review])
async def get_all_reviews():
    return reviews

@review_router.post('/review', status_code=status.HTTP_201_CREATED)
async def create_a_review(review_data: Review) -> dict:
    new_review = review_data.model_dump()
    reviews.append(new_review)
    return new_review

@review_router.delete('/review/{review_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(reviewId: int):
    for review in reviews:
        if review['id'] == reviewId:  # Access the 'id' field of the review dict
            reviews.remove(review)
            return {"message": "review removed successfully"}
    
    # Move the raise outside the loop - only raise if no review was found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="review not found")