# Blockchain-ShOp-Transactio

Overview
The Product Transaction History Viewer is a Python application built using the Tkinter library that allows users to explore the transaction history of various products stored in a CSV file. The application employs the concepts of blockchain technology to represent transaction data as blocks in a blockchain.

Features
Product Selection: Users can choose a product from the list of available products displayed as buttons. Each button corresponds to a unique product in the CSV file.

Blockchain Representation: Upon selecting a product, the application generates a blockchain representing the transaction history of the chosen product. Each transaction is stored as a block in the blockchain, including details such as transaction number, date, product number, product name, price, quantity, customer number, and country.

Dynamic Data Loading: The application dynamically loads product names from the provided CSV file, ensuring that any new products added to the dataset are immediately accessible to users.

User-Friendly Interface: The graphical user interface (GUI) provides an intuitive and visually appealing experience for users. Products are displayed in rows, and transaction history is shown in a formatted manner.

How to Use
Select Product: Click on the product button corresponding to the desired product you want to view the transaction history for.

View Transaction History: The application retrieves transaction data for the selected product from the CSV file and displays it as blocks in a blockchain. Each block contains information about a specific transaction, including timestamps, transaction numbers, and other relevant details.

No Transactions Found: If there are no transactions for the selected product, a message indicating the absence of transactions is displayed.

Requirements
Python: The application requires Python to be installed on the system.
Pandas: The Pandas library is used to read and manipulate data from the CSV file.
Tkinter: Tkinter is utilized for building the graphical user interface.
Hashlib and Time: These libraries are used for generating hashes and timestamps, respectively.
How to Run
Ensure you have Python installed on your system.
Install the required libraries (pandas and tkinter) if you haven't already.
Place your transaction data in a CSV file named transaction_details.csv.
Run the Python script. The GUI will open, allowing you to select and explore the transaction history of different products.
Note
CSV Data Format: The CSV file should contain columns such as TransactionNo, Date, ProductNo, ProductName, Price, Quantity, CustomerNo, and Country to provide accurate transaction details.
Enjoy exploring the transaction history of your products with the Product Transaction History Viewer!





Regenerate
