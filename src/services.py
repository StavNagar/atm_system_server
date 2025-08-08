from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import accounts, actions, Action
from src.logger import log_action, logger

account_bp = Blueprint("account", __name__)

def log_action_per_account(action):
    if action.account_number not in actions:
        actions[action.account_number] = []
    actions[action.account_number].append(action)

@account_bp.route("/accounts/<string:account_number>/balance", methods=["GET"])
@jwt_required()
def get_balance(account_number):
    identity = get_jwt_identity()
    if identity != account_number:
        return jsonify({"error": "Unauthorized"}), 403

    account = accounts.get(account_number)
    if not account:
        return jsonify({"error": "Account not found"}), 404

    logger.info(f"Balance retrieved for {account_number}")
    return jsonify({"balance": account.balance}), 200

@account_bp.route("/accounts/<string:account_number>/deposit", methods=["POST"])
@jwt_required()
def deposit(account_number):
    identity = get_jwt_identity()
    if identity != account_number:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    amount = data.get("amount", 0)
    if amount <= 0:
        return jsonify({"error": "Invalid deposit amount"}), 400

    account = accounts.get(account_number)
    if not account:
        return jsonify({"error": "Account not found"}), 404

    account.update_balance(amount)
    action = Action(account_number, "deposit", amount)
    log_action_per_account(action)
    log_action(account_number, "deposit", amount)

    logger.info(f"Deposit of {amount} to {account_number}")
    return jsonify({"new_balance": account.balance}), 200

@account_bp.route("/accounts/<string:account_number>/withdraw", methods=["POST"])
@jwt_required()
def withdraw(account_number):
    identity = get_jwt_identity()
    if identity != account_number:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    amount = data.get("amount", 0)
    if amount <= 0:
        return jsonify({"error": "Invalid withdrawal amount"}), 400

    account = accounts.get(account_number)
    if not account:
        return jsonify({"error": "Account not found"}), 404

    if account.balance < amount:
        logger.warning(f"Overdraft attempt by {account_number}")
        return jsonify({"error": "Insufficient funds"}), 400

    account.update_balance(-amount)
    action = Action(account_number, "withdraw", amount)
    log_action_per_account(action)
    log_action(account_number, "withdraw", amount)

    logger.info(f"Withdraw of {amount} from {account_number}")
    return jsonify({"new_balance": account.balance}), 200

@account_bp.route("/accounts/<string:account_number>/actions", methods=["GET"])
@jwt_required()
def get_actions(account_number):
    identity = get_jwt_identity()
    if identity != account_number:
        return jsonify({"error": "Unauthorized"}), 403

    account_actions = actions.get(account_number, [])
    result = [{
        "action_type": a.action_type,
        "amount": a.amount,
        "created_at": a.created_at.isoformat()
    } for a in account_actions]

    logger.info(f"Fetched {len(result)} actions for {account_number}")
    return jsonify({"actions": result}), 200
