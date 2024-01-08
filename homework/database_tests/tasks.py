import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

lybrary = client["LibraryDB"]

#Write a query to find all books published on 1949.
published_1949 = lybrary.Books.find({"year published" : 1949})
print(published_1949)

#Retrieve only the titles and authors of all books in the Books collection.
projections = {'title': 1, 'author': 1}
titles_and_authors = lybrary.Books.find({}, projections)
print(titles_and_authors)

