from models.customers import database
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def main():
    return "Welcome!"

@app.route("/users")
def showUsers():
    dbresult = mysqldb.showUsers()
    result = []
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


@app.route("/user", methods=["POST"])
def showUser():
    params = request.json
    dbresult = mysqldb.showUserById(**params)
    user = {
        "id" : dbresult[0],
        "username" : dbresult[1],
        "firstname" : dbresult[2],
        "lastname" : dbresult[3],
        "email" : dbresult[4]            
    }
        
    return jsonify(user)    

if __name__ == "__main__":
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')
    
    app.run(debug=True)
    
    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()