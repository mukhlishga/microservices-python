from app import app
from app.controllers import customers_controller
from flask import Blueprint, request

customers_blueprint = Blueprint("customers_router", __name__)

@app.route("/users", methods=["GET"])
def showUsers():
    return customers_controller.shows()

@app.route("/user", methods=["GET"])
def showUser():
    params = request.json
    return customers_controller.show(**params)

@app.route("/user/insert", methods=["POST"])
def insertUser():
    params = request.json
    return customers_controller.insert(**params)

@app.route("/user/update", methods=["POST"])
def updateUser():
    params = request.json
    return customers_controller.update(**params)

@app.route("/user/delete", methods=["POST"])
def deleteUser():
    params = request.json
    return customers_controller.delete(**params)

@app.route("/user/requesttoken", methods=["GET"])
def requestToken():
    params = request.json
    return customers_controller.token(**params)
