from api.accounts import get_account_balance
from api.accounts import get_multiple_address_balances

from api.tokens import get_token_holder_list
from api.tokens import get_address_erc20_token_holdings
from api.tokens import get_erc20_token_balance

def display_account_balance(address):
    balance_info = get_account_balance(address)
    print("Account Balance:", balance_info['result'])

def display_token_holders(token_address):
    token_holders = get_token_holder_list(token_address)
    token_holders_list = [
        {"TokenHolderAddress": item["TokenHolderAddress"], "TokenHolderQuantity": item["TokenHolderQuantity"]}
        for item in token_holders["result"]
    ]
    return token_holders_list

def enrich_token_holders_with_balances(token_holders_list):
    addresses = [holder['TokenHolderAddress'] for holder in token_holders_list]
    balances_info = get_multiple_address_balances(addresses)
    
    address_to_balance = {item['account']: item['balance'] for item in balances_info['result']}
    
    for holder in token_holders_list:
        holder['EtherBalance'] = address_to_balance.get(holder['TokenHolderAddress'], '0')

    return token_holders_list

def enrich_token_holders_with_tokens_and_balances(enriched_list):
    for holder in enriched_list:
        # Fetch the detailed ERC-20 tokens held by each address
        token_data = get_address_erc20_token_holdings(holder['TokenHolderAddress'])
        holder['ERC20Tokens'] = [
            {
                'TokenAddress': token['TokenAddress'],
                'TokenName': token['TokenName'],
                'TokenSymbol': token['TokenSymbol'],
                'TokenQuantity': token['TokenQuantity'],
                'TokenDivisor': token['TokenDivisor']
            } for token in token_data['result']
        ]
    return enriched_list

def enrich_erc20_token_balances(token_holders_list):
    for holder in token_holders_list:
        for token in holder['ERC20Tokens']:
            balance = get_erc20_token_balance(token['TokenAddress'], holder['TokenHolderAddress'])
            token['TokenBalance'] = balance['result']
    return token_holders_list

def generate_token_balance_matrix(token_holders_list):
    # Extract all unique token addresses
    token_addresses = set()
    for holder in token_holders_list:
        tokens = holder.get('ERC20Tokens', [])
        for token in tokens:
            token_addresses.add(token['TokenAddress'])

    # Sort addresses and tokens to maintain a consistent order
    token_addresses = sorted(token_addresses)
    address_index = {addr: idx for idx, addr in enumerate(token_addresses)}

    # Initialize the matrix
    num_holders = len(token_holders_list)
    num_tokens = len(token_addresses)
    balance_matrix = np.zeros((num_holders, num_tokens))

    # Fill the matrix with balances
    for i, holder in enumerate(token_holders_list):
        for token in holder.get('ERC20Tokens', []):
            token_idx = address_index.get(token['TokenAddress'])
            if token_idx is not None:
                balance_matrix[i, token_idx] = float(token['TokenBalance'])

    return balance_matrix, token_addresses

if __name__ == "__main__":
    test_address = "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d"
    token_holder_list = display_token_holders(test_address)
    token_holder_list_with_balances = enrich_token_holders_with_balances(token_holder_list)
    token_holder_list_with_tokens = enrich_token_holders_with_tokens_and_balances(token_holder_list_with_balances)
    final_token_holder_list = enrich_erc20_token_balances(token_holder_list_with_tokens)

    balance_matrix, token_addresses = generate_token_balance_matrix(final_token_holder_list)

    print("Token Balance Matrix:\n", balance_matrix)
    print("Token Addresses:", token_addresses)
