import re

def is_valid_metamask_address(address):
    # Check if the address starts with "0x" and has a length of 42 characters
    if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return False
    return True

# Example usage:
wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
if is_valid_metamask_address(wallet_address):
    print("Valid MetaMask wallet address.")
else:
    print("Invalid MetaMask wallet address.")
