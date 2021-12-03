from controller import customers
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False # non activating sorting configuration from jsonify
app.config['JWT_SECRET_KEY'] = "testkunci" # a kind of hash key for JWT

jwt = JWTManager(app)

@app.route("/users", methods=["POST"])
def showUsers():
    return customers.shows()

@app.route("/user", methods=["POST"])
def showUser():
    params = request.json
    return customers.show(**params)

@app.route("/requesttoken", methods=["POST"])
def requestToken():
    params = request.json
    return customers.token(**params)

if __name__ == "__main__":
    app.run(debug=True)