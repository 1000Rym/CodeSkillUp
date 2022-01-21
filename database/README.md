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
### What is redis?
- Stands for `Re`mote `Di`ctionary `Se`rver.
- In-Memory Database(Cache)
    - Fast and  performant DB
    - Faster Test
    - Schemless
- Often used as __Cache__ to improve performance.
- Fully-Fledged primary database which can store and persist multiple data-formats.
    - Redis core supports the following features:
        - RediSearch(Elastic Search)
        - RedisGraph(Graph)
        - RedisTimeSeries(Relational)
        - RedisJSON(Documents)
- How does redis persist data?
    - Use replicas to restore.
    - Regular Snapshotting + AOF(Append Only File, Log)
    - Storing data on Separate Infrastructure Storage like(AWS)
- Features:
    - Persist Storing Data
        - Use replicas to restore.
        - Regular Snapshotting + AOF(Append Only File, Log)
        - Storing data on Separate Infrastructure Storage.
    - Redis on Flash: Optimize data stored in RAM(Frequently) and infrequently used data stored in SSD(Infrequently).
    - Scalable: 
        - Clusting: Master and Replicas
        - Sharding: Dive datasets in to smaller chunks and distribute storing horizentally.
    - Active-Active Geo Distributions: High availibility and performance across multiple geographic locations(Availible in Redis Enterprise).

### Installing and configuring Redis
- Installing the redis
    ```shell
    $ redisurl="http://download.redis.io/redis-stable.tar.gz"
    $ curl -s -o redis-stable.tar.gz $redisurl
    $ sudo su root
    $ mkdir -p /usr/local/lib/
    $ chmod a+w /usr/local/lib/
    $ tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
    $ rm redis-stable.tar.gz
    $ cd /usr/local/lib/redis-stable/
    $ make && make install
    ```
- Start up the redis server and check the version, executive bundles.
    ```shell
    $ redis-server
    $ redis-cli --version

    # check the snapshots of executables that come bundled with Redis
    $ls -hFG /usr/local/bin/redis-* | sort
    /usr/local/bin/redis-benchmark*
    /usr/local/bin/redis-check-aof@
    /usr/local/bin/redis-check-rdb@
    /usr/local/bin/redis-cli*
    /usr/local/bin/redis-sentinel@
    /usr/local/bin/redis-server*
    ```
- Configuring Redis
    ```shell
    $ sudo su root
    $ mkdir -p /etc/redis/
    $ touch /etc/redis/6379.conf
    
    # vim and write follwing contents in the 6379.conf
    # /etc/redis/6379.conf
    port              6379
    daemonize         yes
    save              60 1
    bind              127.0.0.1
    tcp-keepalive     300
    dbfilename        dump.rdb
    dir               ./
    rdbcompression    yes

    # config redis-server
    $ redis-server /etc/redis/6379.conf
    ```

- Confirm that the redis server is alive.
    ```shell
    # Check through the redis-cli
    $ redis-cli
    127.0.0.1:6379> ping
    PONG

    # Check the status of redis-servers' process
    $ pgrep redis-server
    ```

- Kill the redis server
    ```shell
    pkill redis-server
    ```

### Adding data via Redis.
A Redis database holds `key:value` pairs and supports commands such as `GET`, `SET`, `DEL` and [hundred of commands](https://redis.io/commands). 
- keys: string type.
- values: string, list, hashes, sets and others such as([geospatial items](https://redis.io/commands#geo)and [stream](https://redis.io/commands#stream)) types.
- Many of Redis commands operate in constant BigO(1) time.

Basic Commands for Using Redis:
```shell
# Set and get Data
127.0.0.1:6379> SET USER1 Benedict
OK

127.0.0.1:6379> GET USER1
"Benedict"

127.0.0.1:6379> GET USER2
(nil)

# MSET(Multiple Set) and MGET(Multiple Get)
127.0.0.1:6379> MSET USER1 Benedict USER2 Carl USER3 Tom
OK

127.0.0.1:6379> MGET USER1 USER2 USER3 USER4
1) "Benedict"
2) "Carl"
3) "Tom"
4) (nil)

# To Check the key Exist
EXISTS USER1
(integer) 1
# Hash Set(HSET) data.
127.0.0.1:6379> HSET team1 member1 Benedeict
127.0.0.1:6379> HSET team1 member2 Carl
127.0.0.1:6379> HSET team1 member3 Kevin

# Hash Multiple SET(HMSET)data
127.0.0.1:6379> HSMET team1 member1 Benedeict member2 Carl Member3 Kevin

# Hash Get ALL(HGETALL) data
127.0.0.1:6379> HGETALL team1
1) "member1"
2) "Benedeict"
3) "member2"
4) "Carl"
5) "member3"
6) "Kevin"

# Clear database and Quit
127.0.0.1:6379> FLUSHDB
OK
127.0.0.1:6379> QUIT
```

### Other data types and commands(Hashes, Sets, Lists)
- Hashes: Commands to operte on hashes begin with an H(HSET, HGET, HGETALL HMSET)
- Sets: Commands to operate with an S, which gets the number of elements at the set value corresponding to a given key.
- Lists: Commands to operate on lists begin with an `L` or `R`. The `L` and `R` refers to which side of the lists' pipe line operate on. There are also commands for `B` which referes blocking which dosen't allow other commands interupt the block command executes.

|Type|Commands|
|:---:|:---|
|Sets| SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, SRANDMEMBER, SREM, SSCAN, SUNION, SUNIONSTORE|
|Hashes| HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, HSET, HSETNX, HSTRLEN, HVALS|
|Lists|	BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, LTRIM, RPOP, RPOPLPUSH, RPUSH, RPUSHX|
|Strings|	APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, INCR, INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN|

### Using Redis with python: redis-py
redis-py is a pythone client library which let you talk to Redis server via python calls.
- Basic
    ```python
    import redis
    r.mset( "user1":"benedict", "user2":"carl", "user3":"kevina"})
    r.get("user2")

    # printed result via python-cli 
    b'carl'

    # result through redis
    127.0.0.1:6379> GET user3
    "kevina"
    ```
- Advanced: Checkout the Example: [PyHats.com](https://realpython.com/python-redis/#example-pyhatscom)
## HBase

## Reference
- Mongo DB: [Python and MongoDB: Connecting to NoSQL Databases](https://realpython.com/introduction-to-mongodb-and-python/)
    - [MonogoDB from Dockerhub](https://hub.docker.com/_/mongo)
- Redis: [How to Use Redis With Python](https://realpython.com/python-redis/)
    - [Introducing Redis](https://www.youtube.com/watch?v=OqCK95AS-YE)
- HBase 
    - [HBase 란 무엇인가?](https://loustler.io/data_eng/what-is-hbase/)
    - [HBase 개념 정리](https://cyberx.tistory.com/164) 
    - HBase with python: [HappyBase](https://happybase.readthedocs.io/en/latest/)  


