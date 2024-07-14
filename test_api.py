import pytest
from main import app
from fastapi.testclient import TestClient
from config.database import usersCollection

client = TestClient(app)

# Test cases for each endpoint
# test case for total posts per user
def test_get_posts_count():
    response = client.get("/users/1/postsCount")
    assert response.status_code == 200
    assert response.json() == 10

# test case for total comments under each post
def test_get_post_comments():
    response = client.get("/posts/1/totalComments")
    assert response.status_code == 200
    assert response.json() == 5

# test case for fetching all comments
def test_fetch_all_comments():
    response = client.get("/comments")
    assert response.status_code == 200
    assert len(response.json()) > 0

# test case for fetching all posts
def test_fetch_all_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

# test case for fetching all users
def test_fetch_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

# test case for adding a new user
def test_add_user():
    new_user = {
        "id": 97,
        "name": "Jane Smith",
        "username": "janesmith",
        "email": "jane.smith@example.com",
        "address": {
        "street": "789 Pine Street",
        "suite": "Suite 101",
        "city": "Los Angeles",
        "zipcode": "90210",
        "geo": {
            "lat": "34.0522",
            "lng": "-118.2437"
        }
        },
        "phone": "+1 (555) 123-7890",
        "website": "janesmith.org",
        "company": {
        "name": "Smith & Co.",
        "catchPhrase": "Excellence in every step",
        "bs": "Consulting and services"
        }
    }
    response = client.post("/users/addUser", json=new_user)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully!"}

# test case for adding a new user with an existing ID
def test_add_existing_user():
    new_user = {
        "id": 97,
        "name": "Jane Smith",
        "username": "janesmith",
        "email": "jane.smith@example.com",
        "address": {
        "street": "789 Pine Street",
        "suite": "Suite 101",
        "city": "Los Angeles",
        "zipcode": "90210",
        "geo": {
            "lat": "34.0522",
            "lng": "-118.2437"
        }
        },
        "phone": "+1 (555) 123-7890",
        "website": "janesmith.org",
        "company": {
        "name": "Smith & Co.",
        "catchPhrase": "Excellence in every step",
        "bs": "Consulting and services"
        }
    }
    response = client.post("/users/addUser", json=new_user)
    assert response.status_code == 400
    assert response.json() == {'detail': "User already exists."}

# test case for updating user details
def test_update_user():
    user_id = 97
    updated_user = {
        "id": 97,
        "name": "Jane Smith",
        "username": "jane",
        "email": "jane.smith@live.com",
        "address": {
        "street": "789 Pine Street",
        "suite": "Suite 120",
        "city": "California",
        "zipcode": "90210",
        "geo": {
            "lat": "34.0522",
            "lng": "-118.2437"
        }
        },
        "phone": "+1 (555) 123-7890",
        "website": "janesmith.org",
        "company": {
        "name": "Smith & Co.",
        "catchPhrase": "Excellence in every step",
        "bs": "Consulting and services"
        }
    }
    response = client.put(f"/users/{user_id}/updateUser", json=updated_user)
    assert response.status_code == 200
    assert response.json() == {"message": "User updated successfully."}

# test case to delete an existing user
def test_delete_user():
    user_id = 97
    response = client.delete(f"/users/{user_id}/deleteUser")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully!"}

# test case to delete a non-existent user
def test_delete_non_existing_user():
    user_id = 93
    response = client.delete(f"/users/{user_id}/deleteUser")
    assert response.status_code == 400
    assert response.json() == {"detail": "User not found."}

