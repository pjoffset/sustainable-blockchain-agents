from app.ai_agent import AIAgent
from app.blockchain_api import BlockchainAPI
from app.energy_optimizer import EnergyOptimizer

def main():
    # Initialize components
    blockchain_api = BlockchainAPI()
    ai_agent = AIAgent(threshold=100)
    optimizer = EnergyOptimizer()

    # Fetch transaction data from blockchain API
    transactions = blockchain_api.fetch_transaction_data()

    if not transactions:
        print("No transaction data available.")
        return

    # Analyze energy usage using AI agent
    average_energy = ai_agent.analyze_energy_usage(transactions)
    recommendations = ai_agent.recommend_optimizations(average_energy)

    print("Energy Analysis:")
    print(f"Average Energy Consumption: {average_energy}")
    print(f"Status: {recommendations['status']}")
    print(f"Recommendation: {recommendations['recommendation']}")

    # Optimize transactions if needed
    if recommendations['status'] == "High Energy Usage":
        optimized_transactions = optimizer.optimize_transactions(transactions)
        print("\nOptimized Transactions:")
        for tx in optimized_transactions:
            print(tx)

if __name__ == "__main__":
    main()
