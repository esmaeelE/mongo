# Using MongoDB database as a NoSQL

Dockerize MongoDB database server with some introduction python scripts.

# Provide the connection details

```
hostname: '127.0.0.1'
port: 27017  # Default MongoDB port
username: mongoadmin  # If authentication is required
password: bdung  # If authentication is required
```

# Usage

In vscode install [Database Client](https://open-vsx.org/extension/cweijan/vscode-database-client2) extension and connect to server.


# Run

Dokckerize server

```
docker-compose up -d
```

python client to communicate to server
```
python3 -m venv env
source env/bin/activate
python3 -m pip install pymongo
```
---

[Based on baeldung article](https://www.baeldung.com/linux/mongodb-as-docker-container)

https://github.com/mongodb/mongo-tools


# CLI

https://github.com/esmaeelE/database/blob/master/scripts/mongodb.md



# Resource
- [fast tutorial](https://github.com/TGITS/docker-compose-examples)

