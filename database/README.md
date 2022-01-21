# Learning Database
In this page, we are going to learn about some database skills, such as [MongoDB](https://www.mongodb.com/), [Redis](https://redis.io/), and [HBase](https://hbase.apache.org/).

## MongoDB
### What is the mongoDB?
MongoDB is a document-oriented and NoSQL(store heterogeneous and structureless data) database solution. 
- Great scalability and flexibility
- Powerful query system.

### What is the NoSQL
NoSQL Database stores heterogeneous and structureless data.

|Property| SQL Database| NoSQL Database|
|:---:|:---:|:---:|
|Data model |Relational|Nonrelational|
|Structure  |Table-based(with columns and rows)|Document-based(key-value pairs, graph, or wide-column)|
|Schema|A predefined and strict schema |A dynamic schema or schemales|
|Query language|SQL(Structured Query Language)|Unstructured|
|Scalability|Vertical|Horizontal|
|ACID Transactions|Supported|Depends on the database|
|Add new Properties|Alter the schema first|Without touch anything|
|Major Products|SQLite, MySQL, Oracle, PostgreSQL, Microsoft SQL Server|DynamoDB, Cassandra, Redis, CouchDB, RethinkDB, RavenDB, MongoDB|

### MongoDB Features
- Query Support: Support standard query types(==, >,<, reqular expression).
- Data accomodataion: Store virtually any kinds of data(structured, partially structured, or polymorphic).
- Scalability: Can handle more queries simply by adding server cluster.
- Flexibility: Adding new properties without disturbing anything.
- Document oriented and schemalessness: Store data without regaring data model.
- Load-banlancing: MongoDB will automatically move data across various shards.
- Automatic failover: Failover to a new one when the primary server is down.
- Management Tools: MMS(MonoDB Management Service)
- Memory Effiecient


### Running the mongo Shell
- Launch The mongo shell
    ```shell
    mongo
    ```

- Basic Commands in MongoDB
    ```shell
    # Check the current database
    > db

    # Check physical database file
    > show dbs

    # Switch connection to new_db
    > use benedict_test
    ```

### Creating Collections and Documents
mongoDB database: physical container for collections of documents.
- Create a collection(A goup of documents)
    ```shell
    > db.tutorial
    benedict_test.tutorial
    ```
- Inserting documents(unit of storage) to the collections.
    - MongoDB stores documents in [BSON(Binary Json)](https://docs.mongodb.com/manual/reference/bson-types/) format.
    - To add a single document use `.insertOne()`
        ```shell
        > db.tutorial.insertOne({
        ... "title":"Reading and Writing CSV Files in Python",
        ... "author":"Jon",
        ... "contributors":[
        ... "Aldren",
        ... "Geir Arne",
        ... "Joanna",
        ... "Jason"
        ... ],
        ... "url":"https://realpython.com/python-csv/"
        ... })
        {
            "acknowledged" : true,
            "insertedId" : ObjectId("61e8f8012356a026a4328d0d")
        }
        ```
    - We can use `.insertMany()` to insert multiple documents as well.
        ```shell
         a = {
             ...
         }
         b = {
             ...
         }
        db.tutorial.insertMany([a,b])
        ```
-  Other Operations:
    - Read operations: `.find()`
    - Update Operations: `updateOne, updateMany(), replaceOne()`
        - Update One, Update Many to update specific specific field.
        - replaceOne: Replace the entire documents.
    - Delete Operations: `.deleteOne(), deleteMany()`

### Running mongo container(docker)
1. Pull the [mongodb](https://hub.docker.com/_/mongo) image from the dockerhub.
1. Run the docker container with default port: 27017
    ``` shell
    docker run -d -p 27017:27017 --name my-mongo mongo:latest
    ```

### Using MongoDB with PyMongo 
[pymongo](https://pypi.org/project/pymongo/) is a python dirver for MongoDB.
- Example Code: [tutorial_pymongo.py](tutorial_pymongo.py)


- Steps for using mongo db with python.
    - Import pymongo and initiailize mongo client.
        ```python
        from pymongo import MongoClient

        # Use default setting : host = 'client', port=27017
        client = MongoClient()
        
        # Use custom port with network address
        client = MonogoClient(host = 'localhost', port = 27017)

        # Use mongodb with url
        client = MongoClient("mongodb://localhost:27017")
        ```    
    - Access DB
        ```python
        # Access db with dictionary-style. 
        db = client['my_db']

        # Access db with mongo shell style.
        db = client.my_db
        ```
    - Specify the collection in db.
        ```python
        my_collection = db.my_db
        ```

    - Make dictionary type storing data.
        ```python
        tutorial1 = {
            "title": "Working With JSON Data in Python",
            "author": "Lucas",
            "contributors": [
                "Aldren",
                "Dan",
                "Joanna"
            ],
            "url": "https://realpython.com/python-json/"
        }

        tutorial2 = {
            "title": "Python's Requests Library (Guide)",
            "author": "Alex",
            "contributors": [
                "Aldren",
                "Brad",
                "Joanna"
            ],
            "url": "https://realpython.com/python-requests/"
        }
        ...
        ```

    - Insert data(One or Many)
        ```python
        import pprint
        
        # Insert One data
        result = my_collection.insert_one(tutorial1)

        # Insert multiple data.
        result = my_collection.insert_many([tutorial2, tutorial3])
        ```

    - Retrieve data with [pprint](https://docs.python.org/3/library/pprint.html#:~:text=The%20pprint%20module%20provides%20a,representation%20may%20not%20be%20loadable.) module.
        ```python
        import pprint

        for doc in my_collectin.find():
            pprint.pprint(doc)
        ```

    - Establish the connection
    Note that the close is an expensive operation. It is suggested to call `.close()` operation when closing the application. 
        ```python
        client.close()
        ```
## Redis

## HBase

## Reference
- Mongo DB: [Python and MongoDB: Connecting to NoSQL Databases](https://realpython.com/introduction-to-mongodb-and-python/)
    - [MonogoDB from Dockerhub](https://hub.docker.com/_/mongo)
- Redis: [How to Use Redis With Python](https://realpython.com/python-redis/)
- HBase 
    - [HBase 란 무엇인가?](https://loustler.io/data_eng/what-is-hbase/)
    - [HBase 개념 정리](https://cyberx.tistory.com/164) 
    - HBase with python: [HappyBase](https://happybase.readthedocs.io/en/latest/)  


