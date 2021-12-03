from app.models.borrows_model import database
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime, requests
from app.models.customers_model import database as cust_db

mysqldb = database()

@jwt_required()
def shows():
    #ambil payload kita dari token
    params = get_jwt_identity()
    dbresult = mysqldb.showBorrowByEmail(**params)
    result = []
    if dbresult is not None:
        for item in dbresult:
            id = json.dumps({"id":item[4]})
            bookdetail = getBookById(id)
            user = {
                "username": item[0],
                "borrowid": item[1],
                "borrowdate": item[2],
                "bookid": item[4],
                "bokname": item[5],
                "author": bookdetail["pengarang"],
                "releaseyear": bookdetail["tahunterbit"],
                "genre": bookdetail["genre"] 
            }

@jwt_required()
def insert(**params):
    token = get_jwt_identity()
    userid = cust_db.showUserByEmail(**token)[0]
    borrowdate = datetime.datetime.now().isoformat()
    id = json.dump({"id":params["bookid"]})
    bookname = getBookById(id)["nama"]
    params.update({
        "userid": userid,
        "borrowdate": borrowdate,
        "bookname": bookname,
        "isactive": 1
    })
    mysqldb.insertBorrow(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

@jwt_required()
def changeStatus(**params):
    mysqldb.updateBorrow(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

def getBookById(data):
    book_data = request.get(url="http:/localhost:8000/bookbyid", data=data)
    return book_data.json()