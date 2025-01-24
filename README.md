# Sustainable Blockchain Agents

## Overview

The **Sustainable Blockchain Agents** project aims to develop AI agents that ensure blockchain technologies operate energy-efficiently. By analyzing energy usage patterns in blockchain transactions, these agents provide recommendations to optimize energy consumption while maintaining performance.



## Installation

To run this project, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. Clone the repository:
git clone <repository-url>
cd sustainable-blockchain-agents


2. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Ensure you have a JSON file named `transactions.json` in the `data/` directory with transaction data structured as follows:
 ```
 [
     {"id": 1, "energy_consumed": 120},
     {"id": 2, "energy_consumed": 80},
     {"id": 3, "energy_consumed": 50},
     {"id": 4, "energy_consumed": 30}
 ]
 ```

2. Run the main script:
python main.py


3. Deploy the smart contract using a tool like Remix or Hardhat to a test Ethereum network (e.g., Ganache).

## Smart Contract

The smart contract `EnergyEfficient.sol` is designed to track energy consumption of transactions on the blockchain. It ensures that only transactions below a specified energy threshold can be added.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request.
