// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EnergyEfficient {
    struct Transaction {
        uint id;
        uint energyConsumed;
    }

    Transaction[] public transactions;

    function addTransaction(uint _id, uint _energyConsumed) public {
        require(_energyConsumed < 100, "Energy consumption exceeds limit!");
        transactions.push(Transaction(_id, _energyConsumed));
    }

    function getTransaction(uint index) public view returns (uint, uint) {
        Transaction memory txn = transactions[index];
        return (txn.id, txn.energyConsumed);
    }

    function totalTransactions() public view returns (uint) {
        return transactions.length;
    }
}
