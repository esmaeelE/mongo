# Using MongoDB database as a NoSQL

Dockerize MongoDB database server with some introduction python scripts.

# Provide the connection details

```
hostname: '127.0.0.1'
port: 27017  # Default MongoDB port
username: mongoadmin  # If authentication is required
password: bdung  # If authentication is required
```
# Run

```
python3 -m venv env
source env/bin/activate
python3 -m pip install pymongo
```


[Based on baeldung article](https://www.baeldung.com/linux/mongodb-as-docker-container)




