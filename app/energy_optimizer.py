class EnergyOptimizer:
    def optimize_transactions(self, transactions):
        optimized_transactions = [
            tx for tx in transactions if tx['energy_consumed'] < 50  # Example filter
        ]
        return optimized_transactions
