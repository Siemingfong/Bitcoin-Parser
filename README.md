# Bitcoin-Parser
Bitcoin’s full-node data grew to 450.84GB on Jan 28, 2023. Most data service providers couldn’t handle all the data on their website for downloading it. For example, Blockchair full-node dump version is snapshots on Jan 20, 2020, which doesn’t support the latest on-chain transactions data. Meaning you have to set up Bitcoin full-node on your own. Let’s do it.

## Environment Requirement
Bitcoin Core
Rosetta homebrew (If you are using a Mac m1 chip)
Python 3.8
Plyvel 1.2.0
Python-bitcoin-blockchain-parser
Bitcoin Core
Download the official software from the website and choose the path you have enough 450.84 GB size. The path is recommended easy to select and let Python fetch your full-node data. For example:
```
/Users/seansie/.bitcoin/blocks
```
## Rosetta homebrew (Mac m1 chop)
I learn from this article teach me how to install and duplicate terminal.
```
softwareupdate — install-rosetta
```
## Python 3.8
I’m doing this from the official website, and I choose 3.8.2 instead of brew install.

## Plyvel 1.2.0 & Python-bitcoin-blockchain-parser
Read the document Plyvel 1.2.0 support Python 3.8 and blockchain-parser only supports Plyvel 1.2.0, so I do this:
```
brew install leveldb
pip3 install plyvel==1.2.0
pip3 install blockchain-parser
```
## Parser Bitcoin full-node to CSV
After the installation part, you can finally parser the Bitcoin data from the Bitcoin Core path. Here is an example of the parser Jan 25, 2023, Bitcoin transaction data:
```
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
```
## Result
The CSV file contains Jan 25, 2023, Bitcoin transactions including Timestamp, Transaction Hash, Inputs, Outputs, and Coinbase. Of course, it could add more columns for other Bitcoin attribute data.
