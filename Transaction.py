import pandas as pd
import hashlib
import time
import tkinter as tk

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
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.timestamp = int(time.time())
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Read data from the CSV file and filter by product name
def read_data_from_csv(file_name, product_name):
    df = pd.read_csv(file_name)
    filtered_data = df[df['ProductName'] == product_name]
    return filtered_data.to_dict(orient="records")

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

# Callback function for product button click
def show_transaction_history(product_name):
    # Read data from the CSV file and filter by product name
    data = read_data_from_csv("transaction_details.csv", product_name)

    if not data:
        history_text.config(state=tk.NORMAL)
        history_text.delete(1.0, tk.END)
        history_text.insert(tk.END, f"No transactions found for the product: {product_name}\n")
        history_text.config(state=tk.DISABLED)
    else:
        # Create the blockchain
        shop_chain = Blockchain()

        # Create blocks for each transaction
        for row in data:
            transaction = create_transaction(row)
            new_block = Block(len(shop_chain.chain), shop_chain.get_latest_block().hash, int(time.time()), transaction)
            shop_chain.add_block(new_block)

        # Display the product name
        history_text.config(state=tk.NORMAL)
        history_text.delete(1.0, tk.END)
        history_text.insert(tk.END, f"TRANSACTION HISTORY\n\n", ('title',))
        for block in shop_chain.chain:
            history_text.insert(tk.END, f"Block #{block.index}\n", 'black_text')
            history_text.insert(tk.END, f"Timestamp: {block.timestamp}\n", 'black_text')
            history_text.insert(tk.END, f"Data: {block.data}\n", 'black_text')
            history_text.insert(tk.END, f"Hash: {block.hash}\n", 'black_text')
            history_text.insert(tk.END, "---------------\n", 'black_text')
        history_text.config(state=tk.DISABLED)

# Initialize Tkinter
root = tk.Tk()
root.title("Product Transaction History")

# Set the background color to dark blue
root.configure(bg="dark blue")

# Add the title at the top
title_label = tk.Label(root, text="Select your product name", font=('Helvetica', 26, 'bold'), bg="black", fg="white")
title_label.pack(pady=10)

# Read data from the CSV file to populate product buttons
data = pd.read_csv("transaction_details.csv")
product_names = data['ProductName'].unique()

# Create a frame to hold button rows
button_frame = tk.Frame(root, bg="orange")
button_frame.pack()

# Create buttons for each product name in rows of four
buttons_per_row = 4
for i, product_name in enumerate(product_names):
    product_button = tk.Button(button_frame, text=product_name, command=lambda name=product_name: show_transaction_history(name), bg="white", fg="black")
    row_num = i // buttons_per_row
    col_num = i % buttons_per_row
    product_button.grid(row=row_num, column=col_num, padx=5, pady=5)

# Create a text widget to display transaction history
history_text = tk.Text(root, wrap=tk.WORD, height=20, width=50, state=tk.DISABLED, bg="white", fg="black")
history_text.tag_configure('title', font=('Helvetica', 16, 'bold'))
history_text.tag_configure('black_text', foreground='black')
history_text.pack(padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
