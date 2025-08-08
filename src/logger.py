import logging

logger = logging.getLogger("atm_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(console_handler)

def log_action(account_number, action_type, amount):
    logger.info(f"Account {account_number} - {action_type.upper()} - Amount: {amount}")
