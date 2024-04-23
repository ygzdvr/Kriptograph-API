import requests
import configparser

def load_api_key(filepath):
    """Load the API key from a configuration file."""
    config = configparser.ConfigParser()
    config.read(filepath)
    return config['etherscan']['api_key']

def get_erc20_token_total_supply(contractaddress):
    """
    Fetches the current total supply of an ERC-20 token given its contract address.

    :param contractaddress: Contract address of the ERC-20 token as a string.
    :return: JSON response containing the total supply of the token.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'stats',
        'action': 'tokensupply',
        'contractaddress': contractaddress,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_erc20_token_balance(contractaddress, address):
    """
    Fetches the current balance of an ERC-20 token for a given address.

    :param contractaddress: Contract address of the ERC-20 token as a string.
    :param address: Ethereum address whose token balance is being queried.
    :return: JSON response containing the token balance of the specified address.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'tokenbalance',
        'contractaddress': contractaddress,
        'address': address,
        'tag': 'latest',  # Use 'latest' for the most recent balance
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_historical_erc20_token_supply(contractaddress, blockno):
    """
    Fetches the historical total supply of an ERC-20 token at a specified block height.

    :param contractaddress: Contract address of the ERC-20 token as a string.
    :param blockno: Block number to retrieve the token supply at.
    :return: JSON response containing the historical total supply of the token.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'stats',
        'action': 'tokensupplyhistory',
        'contractaddress': contractaddress,
        'blockno': blockno,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_historical_erc20_token_balance(contractaddress, address, blockno):
    """
    Fetches the historical balance of an ERC-20 token for a given address at a specified block height.

    :param contractaddress: Contract address of the ERC-20 token as a string.
    :param address: Ethereum address whose token balance is being queried.
    :param blockno: Block number to retrieve the token balance at.
    :return: JSON response containing the historical token balance of the specified address.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'tokenbalancehistory',
        'contractaddress': contractaddress,
        'address': address,
        'blockno': blockno,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_token_holder_list(contractaddress, page=1, offset=10):
    """
    Fetches the current list of ERC-20 token holders and the number of tokens each holds.

    :param contractaddress: Contract address of the ERC-20 token as a string.
    :param page: Page number for pagination.
    :param offset: Number of entries per page.
    :return: JSON response containing the list of token holders.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'token',
        'action': 'tokenholderlist',
        'contractaddress': contractaddress,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_token_info(contractaddress):
    """
    Fetches project information and social media links of an ERC20, ERC721, or ERC1155 token.

    :param contractaddress: Contract address of the token as a string.
    :return: JSON response containing the token information.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'token',
        'action': 'tokeninfo',
        'contractaddress': contractaddress,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_address_erc20_token_holdings(address, page=1, offset=100):
    """
    Fetches all ERC-20 tokens and amounts held by a given address.

    :param address: Ethereum address as a string to check for token balances.
    :param page: Page number for pagination.
    :param offset: Number of entries to display per page.
    :return: JSON response containing the list of ERC-20 tokens and their balances held by the address.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'addresstokenbalance',
        'address': address,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_address_erc721_token_holdings(address, page=1, offset=100):
    """
    Fetches all ERC-721 tokens and amounts held by a given address.

    :param address: Ethereum address as a string to check for NFT holdings.
    :param page: Page number for pagination.
    :param offset: Number of entries to display per page.
    :return: JSON response containing the list of ERC-721 tokens and their balances held by the address.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'addresstokennftbalance',
        'address': address,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_address_erc721_inventory(address, contractaddress, page=1, offset=100):
    """
    Fetches the ERC-721 token inventory of a specific address, filtered by a contract address.

    :param address: Ethereum address as a string to check for NFT inventory.
    :param contractaddress: Contract address of the ERC-721 tokens to filter the inventory.
    :param page: Page number for pagination.
    :param offset: Number of records to display per page.
    :return: JSON response containing the list of ERC-721 token inventory filtered by the contract address.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'addresstokennftinventory',
        'address': address,
        'contractaddress': contractaddress,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    print("Tokens")