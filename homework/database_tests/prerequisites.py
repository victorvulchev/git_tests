import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

lybrary = client["LibraryDB"]
#lybrary.create_collection("Books")
#lybrary.create_collection("Members")
lybrary.Books.insert_many([{"title": "The Hobbit",
                             "author":"J.R.R. Tolkien",
                               "year published": 1937, 
                               "genre":"Fantasy"},
                               {"title": "1984",
                             "author":"George Orwell",
                               "year published": 1949, 
                               "genre":"Dystopian"},
                               {"title": "To Kill a Mockingbird",
                             "author":"Harper Lee",
                               "year published": 1960, 
                               "genre":"Fiction"}])
lybrary.Members.insert_many([{"name" : "Alice Johnson",
                               "membership": "2021-06-15",
                                 "borrowed books": ["The Hobbit", "1984"]},
                                 {"name" : "Bob Smith",
                               "membership": "2020-01-20",
                                 "borrowed books": ["To Kill a Mockingbird"]},
                                 {"name" : "Carol White",
                               "membership": "2022-03-11",
                                 "borrowed books": []}
                                 ])

