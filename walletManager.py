def process_transaction(user_balance: int, tx_amount: int) -> int:
    """
    Process a wallet transaction.
    """
    # BUG: No check for negative amount (stealing funds)
    # BUG: No check for overdraft (balance < amount)
    new_balance = user_balance - tx_amount
    return new_balance