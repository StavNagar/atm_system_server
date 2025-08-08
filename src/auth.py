from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from src.models import accounts, Account
from src.logger import logger


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    account_number = data.get("account_number")
    password = data.get("password")

    if not account_number or not password:
        return jsonify({"error": "Missing account_number or password"}), 400

    if account_number in accounts:
        return jsonify({"error": "Account already exists"}), 400

    accounts[account_number] = Account(account_number, password)
    logger.info(f"Registered new account: {account_number}")
    return jsonify({"message": "Account created"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    account_number = data.get("account_number")
    password = data.get("password")

    account = accounts.get(account_number)
    if not account or not account.check_password(password):
        logger.warning(f"Failed login attempt for account: {account_number}")
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=account_number)
    logger.info(f"Account {account_number} logged in")
    return jsonify({"access_token": token}), 200
