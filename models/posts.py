from pydantic import BaseModel

# pydantic model for posts
class Posts(BaseModel):
    userId: int
    id: int
    title: str
    body: str