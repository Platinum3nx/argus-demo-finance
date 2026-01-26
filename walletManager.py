# ##Bugged code
# def process_transaction(user_balance: int, tx_amount: int) -> int:
#     """
#     Process a wallet transaction.
#     """
#     # BUG: No check for negative amount (stealing funds)
#     # BUG: No check for overdraft (balance < amount)
#     new_balance = user_balance - tx_amount
#     return new_balance

##Working code
class WalletManager:
    def __init__(self, initial_balance=0.0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        # FIX: We added 'amount > 0' to prevent negative withdrawals
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
