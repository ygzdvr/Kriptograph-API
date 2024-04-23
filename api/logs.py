import requests
import configparser

def load_api_key(filepath):
    """Load the API key from a configuration file."""
    config = configparser.ConfigParser()
    config.read(filepath)
    return config['etherscan']['api_key']

def get_event_logs_by_address(address, fromBlock, toBlock, page=1, offset=1000):
    """
    Fetches event logs from an Ethereum address, with optional filtering by block range.

    :param address: Ethereum address as a string to check for logs.
    :param fromBlock: Starting block number for the log search.
    :param toBlock: Ending block number for the log search.
    :param page: Page number for pagination.
    :param offset: Number of logs displayed per page.
    :return: JSON response containing event logs.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'logs',
        'action': 'getLogs',
        'address': address,
        'fromBlock': fromBlock,
        'toBlock': toBlock,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def get_event_logs_by_topics(fromBlock, toBlock, topics, page=1, offset=1000):
    """
    Fetches event logs within a block range, filtered by topics.

    :param fromBlock: Starting block number for the log search.
    :param toBlock: Ending block number for the log search.
    :param topics: Dictionary of topics and their corresponding operators. 
                   Example: {'topic0': '0xdd...', 'topic1': '0x00...', 'topic0_1_opr': 'and'}
    :param page: Page number for pagination.
    :param offset: Number of logs displayed per page.
    :return: JSON response containing event logs filtered by topics.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'logs',
        'action': 'getLogs',
        'fromBlock': fromBlock,
        'toBlock': toBlock,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    # Merge topic filters into the parameters
    params.update(topics)
    
    response = requests.get(url, params=params)
    return response.json()

def get_event_logs_by_address_and_topics(address, fromBlock, toBlock, topics, page=1, offset=1000):
    """
    Fetches event logs from an Ethereum address, filtered by topics and within a specified block range.

    :param address: Ethereum address as a string to check for logs.
    :param fromBlock: Starting block number for the log search.
    :param toBlock: Ending block number for the log search.
    :param topics: Dictionary of topics and their corresponding operators. 
                   Example: {'topic0': '0x27...', 'topic1': '0x00...', 'topic0_1_opr': 'and'}
    :param page: Page number for pagination.
    :param offset: Number of logs displayed per page.
    :return: JSON response containing event logs filtered by topics.
    """
    api_key = load_api_key('config/credentials.ini')
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'logs',
        'action': 'getLogs',
        'address': address,
        'fromBlock': fromBlock,
        'toBlock': toBlock,
        'page': page,
        'offset': offset,
        'apikey': api_key
    }
    # Merge topic filters into the parameters
    params.update(topics)
    
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    print("Logs")