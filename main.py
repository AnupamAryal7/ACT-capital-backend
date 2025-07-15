from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

reviews = [
    {
        "id": 1,
        "author": "Sushma Thapa",
        "description": "Instructors were patient and professional. I passed my driving test on the first try!",
        "created_at": "2024-11-10T09:30:00",
    },
    {
        "id": 2,
        "author": "Ramesh Shrestha",
        "description": "Very flexible scheduling and clean vehicles. Highly recommend ACT Capital Driving School.",
        "created_at": "2024-11-15T14:45:00",
    },
    {
        "id": 3,
        "author": "Manita KC",
        "description": "Helped me overcome my fear of driving. The instructors were calm and encouraging.",
        "created_at": "2024-12-01T11:00:00",
    },
    {
        "id": 4,
        "author": "Bikash Lama",
        "description": "Great experience! They teach both traffic rules and practical techniques clearly.",
        "created_at": "2024-12-10T16:20:00",
    },
    {
        "id": 5,
        "author": "Pooja Maharjan",
        "description": "Loved the friendly environment. I learned a lot more than expected!",
        "created_at": "2024-12-18T13:10:00",
    },
    {
        "id": 6,
        "author": "Sagar Dhakal",
        "description": "Affordable fees and excellent teaching. Passed license test easily!",
        "created_at": "2025-01-05T08:55:00",
    },
]
class Review(BaseModel):
    id: int
    author: str
    description: str
    created_at: str



@app.get('/')
async def root():
    return{"message": "backend is running"}

@app.get('/review', response_model=List[Review])
async def get_all_reviews():
    return reviews

@app.post('/review', status_code=status.HTTP_201_CREATED)
async def create_a_review(review_data: Review) -> dict:
    new_review = review_data.model_dump()
    reviews.append(new_review)
    return new_review

@app.delete('/review/{review_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(reviewId: int):
    for review in reviews:
        if review['id'] == reviewId:  # Access the 'id' field of the review dict
            reviews.remove(review)
            return {"message": "review removed successfully"}
    
    # Move the raise outside the loop - only raise if no review was found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="review not found")