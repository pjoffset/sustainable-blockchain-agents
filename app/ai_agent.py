import json

class AIAgent:
    def __init__(self, threshold=100):
        self.threshold = threshold  # Energy consumption threshold

    def analyze_energy_usage(self, transactions):
        total_energy = sum(tx['energy_consumed'] for tx in transactions)
        average_energy = total_energy / len(transactions)
        return average_energy

    def recommend_optimizations(self, average_energy):
        if average_energy > self.threshold:
            return {
                "status": "High Energy Usage",
                "recommendation": "Reduce transaction frequency or optimize smart contract code."
            }
        return {
            "status": "Energy Efficient",
            "recommendation": "No changes needed."
        }
