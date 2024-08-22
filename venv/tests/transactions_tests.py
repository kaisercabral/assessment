class TransactionsTests:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        """Adds a transaction to the list."""
        self.transactions.append(transaction)
        print(f"Transaction {transaction} added.")

    def validate_transaction(self, transaction):
        """Validates if a specific transaction is in the list."""
        if transaction in self.transactions:
            print(f"Transaction {transaction} is valid.")
            return True
        else:
            print(f"Transaction {transaction} is not found.")
            return False

    # Example usage:
    tests = TransactionsTests()
    tests.add_transaction("TX123")
    tests.validate_transaction("TX123")
    tests.validate_transaction("TX999")