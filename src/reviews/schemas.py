from pydantic import BaseModel
class Review(BaseModel):
    id: int
    author: str
    description: str
    created_at: str
