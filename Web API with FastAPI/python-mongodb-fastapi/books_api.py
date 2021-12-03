from pymongo import MongoClient
from models.books_model import database as db
import csv, json
import json
from bson import ObjectId

db = db()

def objIdToStr(obj):
    return str(obj["_id"])

def search_book_by_name(**params):
    data_list = []
    for book in db.searchBookByName(**params):
        book["_id"] = objIdToStr(book)
        data_list.append(book)
    return data_list

def search_books():
    data_list = []
    for book in db.showBooks():
        book["_id"] = objIdToStr(book)
        data_list.append(book)
    return data_list

def search_books_id(**params):
    result = db.showBookById(**params)
    result["_id"] = objIdToStr(result)
    return result