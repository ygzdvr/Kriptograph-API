import requests
import configparser

def load_api_key(filepath):
    """Load the API key from a configuration file."""
    config = configparser.ConfigParser()
    config.read(filepath)
    return config['etherscan']['api_key']

def get_account_balance(address):
    """Fetch the account balance for a given Ethereum address using the Etherscan API."""
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_multiple_address_balances(addresses):
    """
    Fetches the Ether balances for multiple addresses in a single API call.

    :param addresses: List of Ethereum addresses as strings.
    :return: JSON response containing balances.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'balancemulti',
        'address': ','.join(addresses),
        'tag': 'latest',
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_transactions_by_address(address, startblock=0, endblock=99999999, page=1, offset=10, sort='asc'):
    """
    Fetches a list of normal transactions performed by an address.

    :param address: Ethereum address as a string.
    :param startblock: Starting block number for transaction search.
    :param endblock: Ending block number for transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of transactions.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_internal_transactions(address, startblock=0, endblock=2702578, page=1, offset=10, sort='asc'):
    """
    Fetches a list of internal transactions performed by an address with optional pagination.

    :param address: Ethereum address as a string.
    :param startblock: Starting block number for transaction search.
    :param endblock: Ending block number for transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of internal transactions.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txlistinternal',
        'address': address,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_internal_transactions_by_hash(txhash):
    """
    Fetches a list of internal transactions performed within a transaction, identified by the transaction hash.

    :param txhash: The transaction hash as a string.
    :return: JSON response containing the list of internal transactions.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txlistinternal',
        'txhash': txhash,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_internal_transactions_by_block_range(startblock, endblock, page=1, offset=10, sort='asc'):
    """
    Fetches a list of internal transactions performed within a specified block range.

    :param startblock: The starting block number for the transaction search.
    :param endblock: The ending block number for the transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of internal transactions.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txlistinternal',
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_erc20_token_transfers(address, contractaddress=None, startblock=0, endblock=27025780, page=1, offset=100, sort='asc'):
    """
    Fetches a list of ERC-20 token transfer events by address, with optional filtering by token contract.

    :param address: Ethereum address as a string.
    :param contractaddress: Contract address of the ERC-20 token (optional).
    :param startblock: Starting block number for transaction search.
    :param endblock: Ending block number for transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of token transfers.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': address,
        'contractaddress': contractaddress,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_erc721_token_transfers(address, contractaddress=None, startblock=0, endblock=27025780, page=1, offset=100, sort='asc'):
    """
    Fetches a list of ERC-721 token transfer events by address, with optional filtering by token contract.

    :param address: Ethereum address as a string.
    :param contractaddress: Contract address of the ERC-721 token (optional).
    :param startblock: Starting block number for transaction search.
    :param endblock: Ending block number for transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of ERC-721 token transfers.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'tokennfttx',
        'address': address,
        'contractaddress': contractaddress,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_erc1155_token_transfers(address, contractaddress=None, startblock=0, endblock=99999999, page=1, offset=100, sort='asc'):
    """
    Fetches a list of ERC-1155 token transfer events by address, with optional filtering by token contract.

    :param address: Ethereum address as a string.
    :param contractaddress: Contract address of the ERC-1155 token (optional).
    :param startblock: Starting block number for transaction search.
    :param endblock: Ending block number for transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of ERC-1155 token transfers.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'token1155tx',
        'address': address,
        'contractaddress': contractaddress,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_mined_blocks(address, blocktype='blocks', page=1, offset=10):
    """
    Fetches a list of blocks validated by an address.

    :param address: Ethereum address as a string.
    :param blocktype: Type of blocks to fetch ('blocks' for canonical blocks, 'uncles' for uncle blocks).
    :param page: Page number for pagination.
    :param offset: Number of blocks to display per page.
    :return: JSON response containing the list of mined blocks.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'getminedblocks',
        'address': address,
        'blocktype': blocktype,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_beacon_chain_withdrawals(address, startblock=0, endblock=99999999, page=1, offset=100, sort='asc'):
    """
    Fetches beacon chain withdrawals made to an address over a specified block range.

    :param address: Ethereum address as a string.
    :param startblock: Starting block number for the transaction search.
    :param endblock: Ending block number for the transaction search.
    :param page: Page number for pagination.
    :param offset: Number of transactions per page.
    :param sort: Sorting order, 'asc' for ascending, 'desc' for descending.
    :return: JSON response containing the list of beacon chain withdrawals.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txsBeaconWithdrawal',
        'address': address,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_historical_ether_balance(address, blockno):
    """
    Fetches the historical Ether balance of an address at a specified block height.

    :param address: Ethereum address as a string.
    :param blockno: Block number to check the balance at.
    :return: JSON response containing the Ether balance at the specified block.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'balancehistory',
        'address': address,
        'blockno': blockno,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    addresses = [
        "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a",
        "0x63a9975ba31b0b9626b34300f7f627147df1f526",
        "0x198ef1ec325a96cc354c7266a038be8b5c558f67"]

    balances = get_multiple_address_balances(addresses)
    print(balances)