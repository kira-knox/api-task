from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
# client = MongoClient('mongodb://localhost:27017/')
# db = client.user_data
# postsCollection = db['posts']
# commentsCollection = db['comments']
# usersCollection = db['users']

# Mongo connection
client = MongoClient('localhost', 27017)
# try to ping to Mongo to check whether connection is successful
try:
   client.admin.command('ping')
   print("Pinged your deployment successfully!")
except ConnectionFailure:
   print("Server not available")

db = client.user_data
postsCollection = db['posts']
commentsCollection = db['comments']
usersCollection = db['users']