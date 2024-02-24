from pymongo import MongoClient
import datetime
from datetime import timedelta
import pprint

# client = MongoClient('mongodb://localhost:27017/')

# Provide the connection details
hostname = '127.0.0.1'
port = 27017  # Default MongoDB port
username = 'mongoadmin'  # If authentication is required
password = 'bdung'  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)


db = client['baeldung']
collection = db['articles']

print('Droping collection')
db.collection.drop()

entry1 = {
      "author": "GC",
      "text": "My first blog post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow() - timedelta(days=1)
      }

entry2 = {
      "author": "GICC",
      "text": "My second blog post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow()
      }

entry_inserted_id = db.collection.insert_one(entry1).inserted_id
print( "Inserted entry: " + str(entry_inserted_id) )

entry_inserted_id = db.collection.insert_one(entry2).inserted_id
print( "Inserted entry: " + str(entry_inserted_id) )

for a in db.collection.find():
  pprint.pprint(a)

