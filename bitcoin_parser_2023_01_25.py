import os
import csv
from blockchain_parser.blockchain import Blockchain
from datetime import timedelta, datetime

# Instantiate the blockchain
blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))

# Define the date range
start_date = datetime(2023, 1, 25, 0, 0)
end_date = datetime(2023, 1, 25, 23, 23)

with open("transaction_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(["Timestamp", "Transaction Hash", "Inputs", "Outputs", "Coinbase"])
    # Iterate through all blocks
    for block in blockchain.get_unordered_blocks():
        block_time = block.header.timestamp
        print(block_time)
        # Check if the block timestamp is within the last two days
        if start_date <= block_time <= end_date :
            for tx in block.transactions:
                coinbase = tx.inputs[0]
                # Write the transaction data to the csv file
                writer.writerow([block.header.timestamp, tx.hash, tx.inputs, tx.outputs, coinbase])
