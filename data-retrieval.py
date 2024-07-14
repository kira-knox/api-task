# script to retrieve data for MongoDB from jsonplaceholder website
import requests
from pymongo import MongoClient

resourceList = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']

for resource in resourceList:
    url = (f"https://jsonplaceholder.typicode.com/{resource}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        client = MongoClient('mongodb://localhost:27017/')
        db = client.user_data
        collection = db[resource]
        collection.insert_many(data)
