# pip install mongoengine

from mongoengine import connect
from mongoengine import Document, IntField, StringField, DynamicDocument

connection = connect(db='rentalfilm', host='localhost', port=27017) # database name, host, port

class customers(Document): # 'customers' = collection name
    _id = IntField(required=True) # customer's fileds/columns
    username = StringField(required=True, max_length=70) # customer's fileds/columns
    fullname = StringField(required=True, max_length=20) # customer's fileds/columns
    email = StringField(required=True, max_length=20) # customer's fileds/columns