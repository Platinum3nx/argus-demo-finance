def deposit(balance: int, amount: int) -> int:
    """Deposit money into the wallet."""
    if amount < 0:
        return balance
    return balance + amount


def withdraw(balance: int, amount: int) -> int:
    """Withdraw money from the wallet."""
    if amount < 0:
        return balance
    if amount > balance:
        return balance
    return balance - amount


def transfer(sender_balance: int, receiver_balance: int, amount: int) -> tuple:
    """Transfer money between two wallets."""
    if amount < 0:
        return (sender_balance, receiver_balance)
    if amount > sender_balance:
        return (sender_balance, receiver_balance)
    new_sender = sender_balance - amount
    new_receiver = receiver_balance + amount
    return (new_sender, new_receiver)


def get_balance(balance: int) -> int:
    """Return the current balance."""
    return balance
