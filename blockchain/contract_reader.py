import json
import logging
from web3 import Web3
import config

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

def fetch_total_supply(contract_address):
    """Fetches total supply and decimals for any ERC-20 token from the contract."""
    
    try:
        # Minimal ABI for totalSupply and decimals functions
        minimal_abi = json.dumps([
            {
                "constant": True,
                "inputs": [],
                "name": "totalSupply",
                "outputs": [{"name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            }
        ])

        logging.debug(f"Minimal ABI being used: {minimal_abi}")
        
        # Load contract using the minimal ABI
        contract = web3.eth.contract(address=contract_address, abi=json.loads(minimal_abi))

        # Fetch total supply
        logging.debug(f"Calling totalSupply function on contract: {contract_address}")
        total_supply = contract.functions.totalSupply().call()
        logging.debug(f"Total Supply (raw): {total_supply}")

        # Fetch decimals
        logging.debug(f"Calling decimals function on contract: {contract_address}")
        decimals = contract.functions.decimals().call()
        logging.debug(f"Decimals: {decimals}")

        # Adjust total supply based on the token's decimals
        adjusted_total_supply = total_supply / (10 ** decimals)
        return f"Total Supply: {adjusted_total_supply}"

    except Exception as e:
        logging.error(f"Error reading contract: {e}")
        return f"Error reading contract: {str(e)}"

