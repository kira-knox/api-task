from fastapi import APIRouter, HTTPException
from config.database import usersCollection, postsCollection, commentsCollection
from models.users import User
from bson import ObjectId
from schemas.schemas import user_list_serial, comment_list_serial, post_list_serial

router = APIRouter()

# Endpoints
@router.get('/')
async def root():
    return {"message": "Go to /docs"}

# get a list of all comments
@router.get('/comments')
async def fetch_all_comments():
    comments = comment_list_serial(commentsCollection.find())
    return comments

# get a list of all posts
@router.get('/posts')
async def fetch_all_posts():
    posts = post_list_serial(postsCollection.find())
    return posts

# get a list of all users
@router.get('/users')
async def fetch_all_users():
    users = user_list_serial(usersCollection.find())
    return users

# get the total number of posts from each user
@router.get('/users/{user_id}/postsCount')
async def get_posts_count(user_id: int):
    postsCount = postsCollection.count_documents({"userId":user_id})
    return postsCount

# get the total comments under each post
@router.get('/posts/{post_id}/totalComments')
async def get_comments_per_post(post_id: int):
    comments = list(commentsCollection.find({"postId": post_id}))
    commentsCount = len(comments)
    return commentsCount

# add a user
@router.post('/users/addUser')
async def add_user(user: User):
    # check if user already exists
    if usersCollection.find_one({"id": user.id}):
        raise HTTPException(status_code=400, detail="User already exists.")
    usersCollection.insert_one(user.model_dump())
    return {"message": "User created successfully!"}

# update user details
@router.put('/users/{user_id}/updateUser')
async def update_user(user_id: int, user: User):
    # check if user does not exist
    if usersCollection.find_one({"id": user_id}) is None:
        raise HTTPException(status_code=400, detail="User not found.")
    else:
        usersCollection.find_one_and_update({"id":user_id}, {"$set": user.model_dump(by_alias=True)})
        return {"message": "User updated successfully."}

# delete a user
@router.delete('/users/{user_id}/deleteUser')
async def delete_user(user_id: int):
    # check if user does not exist
    if usersCollection.find_one({"id": user_id}) is None:
        raise HTTPException(status_code=400, detail="User not found.")
    else:
        usersCollection.find_one_and_delete({"id":user_id})
        return {"message": "User deleted successfully!"}
