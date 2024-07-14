def user_individual_serial(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "address": user["address"],
        "phone": user["phone"],
        "website": user["website"],
        "company": user["company"]
    }

def user_list_serial(users) -> list:
    return[user_individual_serial(user) for user in users]

def comment_individual_serial(comment) -> dict:
    return {
        "_id": str(comment["_id"]),
        "postId": comment["postId"],
        "id": comment["id"],
        "name": comment["name"],
        "email": comment["email"],
        "body": comment["body"]
    }

def comment_list_serial(comments) -> list:
    return[comment_individual_serial(comment) for comment in comments]

def post_individual_serial(post) -> dict:
    return {
        "_id": str(post["_id"]),
        "userId": post["userId"],
        "id": post["id"],
        "title": post["title"],
        "body": post["body"]
    }

def post_list_serial(posts) -> list:
    return[post_individual_serial(post) for post in posts]
