### Ethereum TestNet Example: (Goerli)
# pip install web3

from web3 import Web3

api = "<QuickNode Goerli API>"
w3 = Web3(Web3.HTTPProvider(api))
w3.eth.get_block_number()   # get latest block details
w3.eth.block_number         # get latest block number

Documentation:
QuickNode API: https://www.quicknode.com
Web3.py:       https://web3py.readthedocs.io/en/stable/

