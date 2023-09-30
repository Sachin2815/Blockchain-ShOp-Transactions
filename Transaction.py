import hashlib
import time

class BlockchainTransaction:
    def __init__(self, TransactionNo, ProductNo, ProductName, Price, Quantity, CustomerNo, Country):
        self.TransactionNo = TransactionNo
        self.ProductNo = ProductNo
        self.ProductName = ProductName
        self.Price = Price
        self.Quantity = Quantity
        self.CustomerNo = CustomerNo
        self.Country = Country
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = (str(self.TransactionNo) + str(self.ProductNo) + self.ProductName +
                str(self.Price) + str(self.Quantity) + str(self.CustomerNo) + self.Country +
                str(self.timestamp) + str(self.nonce))
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_transaction(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f"Transaction No: {self.TransactionNo}\nProduct No: {self.ProductNo}\nProduct Name: {self.ProductName}\nPrice: {self.Price}\nQuantity: {self.Quantity}\nCustomer No: {self.CustomerNo}\nCountry: {self.Country}\nTimestamp: {self.timestamp}\nNonce: {self.nonce}\nHash: {self.hash}"

class Block:
    def __init__(self):
        self.transactions = []
        self.previous_hash = ""
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = "".join(str(transaction.hash) for transaction in self.transactions) + self.previous_hash + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block()

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.get_latest_block().transactions.append(transaction)

    def mine_pending_transactions(self):
        new_block = Block()
        new_block.transactions = self.get_latest_block().transactions.copy()
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.get_latest_block().transactions = []

    def print_blockchain(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i} - Hash: {block.hash}")
            for transaction in block.transactions:
                print(transaction)
            print("="*30)

# Example usage:
blockchain = Blockchain()

# Create and add transactions
transaction1 = BlockchainTransaction(1, 1001, "Widget", 10.99, 5, "Cust123", "US")
transaction2 = BlockchainTransaction(2, 1002, "Gadget", 25.49, 2, "Cust456", "UK")

blockchain.add_transaction(transaction1)
blockchain.add_transaction(transaction2)

# Mine pending transactions
blockchain.mine_pending_transactions()

# Print the blockchain
blockchain.print_blockchain()
# ... (previous code remains unchanged)

# Example usage:
blockchain = Blockchain()

# Create and add transactions
transaction1 = BlockchainTransaction(1, 1001, "Widget", 10.99, 5, "Cust123", "US")
transaction2 = BlockchainTransaction(2, 1002, "Gadget", 25.49, 2, "Cust456", "UK")
transaction3 = BlockchainTransaction(3, 1003, "Smartphone", 299.99, 1, "Cust789", "CA")
transaction4 = BlockchainTransaction(4, 1004, "Laptop", 599.99, 1, "Cust101", "AU")

blockchain.add_transaction(transaction1)
blockchain.add_transaction(transaction2)
blockchain.add_transaction(transaction3)
blockchain.add_transaction(transaction4)

# Mine pending transactions
blockchain.mine_pending_transactions()

# Print the blockchain
print("Blockchain:")
blockchain.print_blockchain()
