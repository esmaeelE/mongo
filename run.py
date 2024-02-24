from pymongo import MongoClient
import pprint

# Provide the connection details
hostname = '127.0.0.1'
port = 27017  # Default MongoDB port
username = 'mongoadmin'  # If authentication is required
password = 'bdung'  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)

db = client['baeldung']

collection = db['articles']
# print(collection)

for a in collection.find():
  pprint.pprint(a)

client.close()
