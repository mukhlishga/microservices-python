from pymongo import MongoClient
from bson import ObjectId

class database:
    def __init__(self):
        try:
            self.nosql_db = MongoClient(host='localhost', port=27017)
            self.db = self.nosql_db.perpustakaan # your database name
            self.mongo_col = self.db.books # your collection/table name
            print('database connected')
        except Exception as e:
            print(e)

    def insertBook(self, document):
        self.mongo_col.insert_one(document)

    def searchBookByName(self, key):
        query = {'nama' : {'$regex' : key, '$options' : 'i'}} # regex = include string, i = case insensitive
        result = self.mongo_col.find(query)
        return result

    def showBooks(self):
        result = self.mongo_col.find()
        return result
        
    def showBookById(self, key):
        query = {'_id' : ObjectId(key)}
        result = self.mongo_col.find(query)
        return result

    def updateBookById(self, params):
        query = {'_id' : ObjectId(params['_id'])}
        newValues = {'$set': {'nama': params['nama'], 'pengarang': params['pengarang'], 'tahun terbit': params['tahun terbit'], 'genre': params['genre']}}
        self.mongo_col.update_one(query, newValues)

    def deleteBookById(self,key):
        query = {'_id' : ObjectId(key)}
        result = self.mongo_col.remove(query)
        return result