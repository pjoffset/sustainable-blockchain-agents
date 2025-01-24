import json

class BlockchainAPI:
    def __init__(self, data_file="data/transactions.json"):
        self.data_file = data_file

    def fetch_transaction_data(self):
        try:
            with open(self.data_file, 'r') as file:
                transactions = json.load(file)
            return transactions
        except FileNotFoundError:
            print("Transaction data file not found.")
            return []
