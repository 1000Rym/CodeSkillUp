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

### Using MongoDB with PyMongo 
[pymongo](https://pypi.org/project/pymongo/) is a python dirver for MongoDB.
```shell
pymongo
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


