import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")


print(client.list_database_names())

new_db = client["new-db"]


print(new_db.list_collection_names())

doc_id = new_db.test_collection.insert_one({"a":1})

print(doc_id)

print(new_db.list_collection_names())


