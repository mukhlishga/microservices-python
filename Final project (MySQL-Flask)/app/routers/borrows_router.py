from app import app
from app.controllers import borrows_controller
from flask import Blueprint, request

borrows_blueprint = Blueprint("borrows_router", __name__)

@app.route("/borrows", methods=["GET"])
def showBorrow():
    return borrows_controller.shows()

@app.route("/borrow/inserts", methods=["POST"])
def insertBorrow():
    params = request.json
    return borrows_controller.insert()

@app.route("/borrow/status", methods=["POST"])
def changeStatusBorrow():
    return borrows_controller.changeStatus()