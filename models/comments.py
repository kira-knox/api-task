from pydantic import BaseModel

# pydantic model for comments
class Comments(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str