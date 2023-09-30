import pandas as pd
import hashlib
import time

# Define the Block class
class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_str = f"{self.index}{self.previous_hash}{self.timestamp}{str(self.data)}{self.nonce}"
        return hashlib.sha256(data_str.encode()).hexdigest()

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", str(int(time.time())), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.timestamp = str(int(time.time()))
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Read data from the CSV file
def read_data_from_csv(file_name):
    df = pd.read_csv(file_name)
    return df.to_dict(orient="records")

# Create a transaction dictionary
def create_transaction(row):
    transaction = {
        "TransactionNo": row["TransactionNo"],
        "Date": row["Date"],
        "ProductNo": row["ProductNo"],
        "ProductName": row["ProductName"],
        "Price": row["Price"],
        "Quantity": row["Quantity"],
        "CustomerNo": row["CustomerNo"],
        "Country": row["Country"],
    }
    return transaction

if __name__ == "__main__":
    # Read data from the CSV file
    data = read_data_from_csv("transaction_details.csv")

    # Create the blockchain
    shop_chain = Blockchain()

    # Create blocks for each transaction
    for row in data:
        transaction = create_transaction(row)
        new_block = Block(len(shop_chain.chain), shop_chain.get_latest_block().hash, str(int(time.time())), transaction)
        shop_chain.add_block(new_block)

    # Display the blockchain
    for block in shop_chain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("---------------")

