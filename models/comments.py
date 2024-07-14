from pydantic import BaseModel

class Comments(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str