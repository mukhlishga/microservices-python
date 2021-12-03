from models.customers import database
from flask import Flask, jsonify, request
from flask_jwt_extended import *
import datetime

mysqldb = database()

@jwt_required()
def shows():
    dbresult = mysqldb.showUsers()
    result = []
    print(dbresult)
    for items in dbresult:
        user = {
            "id" : items[0],
            "username" : items[1],
            "firstname" : items[2],
            "lastname" : items[3],
            "email" : items[4]            
        }
        result.append(user)
        
    return jsonify(result)

def show(**params):
    dbresult = mysqldb.showUserById(**params)
    user = {
        "id" : dbresult[0],
        "username" : dbresult[1],
        "firstname" : dbresult[2],
        "lastname" : dbresult[3],
        "email" : dbresult[4]            
    }
        
    return jsonify(user)

def token(**params):
    dbresult = mysqldb.showUserByEmail(**params)
    if dbresult is not None:
        user = {
            "username" : dbresult[1],
            "email" : dbresult[4]            
        }
        expires = datetime.timedelta(days=1)
        expires_refresh = datetime.timedelta(days=3)
        access_token = create_access_token(user, fresh=True, expires_delta=expires)
        
        data = {
            "data": user,
            "token_access": access_token
        }
    else:
        data = {
            "message":"Email tidak terdaftar"
        }
        
    return jsonify(data)