from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone


accounts = {}
actions = {}

class Account:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password_hash = generate_password_hash(password)
        self.balance = 0.0
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def update_balance(self, amount):
        self.balance += amount
        self.updated_at = datetime.now(timezone.utc)

class Action:
    def __init__(self, account_number, action_type, amount):
        self.account_number = account_number
        self.action_type = action_type
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
