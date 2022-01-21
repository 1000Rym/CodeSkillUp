from pymongo import MongoClient
import pprint

def main():
    # Initilize mongo client
    client = MongoClient(host='localhost', port=27017)
    
    # Access DB
    db = client['my_db']
    
    # specicy the collection(table).
    my_collection = db.my_db
    
    # Make the inserting data
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
    tutorial3 = {
        "title": "Object-Oriented Programming (OOP) in Python 3",
        "author": "David",
        "contributors": [
            "Aldren",
            "Joanna",
            "Jacob"
        ],
        "url": "https://realpython.com/python3-object-oriented-programming/"
    }
    
    # insert data(One, Many)
    my_collection.insert_one(tutorial1)
    my_collection.insert_many([tutorial2, tutorial3])
    
    
    # Retrive inserted data.
    for doc in my_collection.find():
        pprint.pprint(doc)

    # Establish the db connection
    client.close()    

if __name__ == '__main__':
    main()