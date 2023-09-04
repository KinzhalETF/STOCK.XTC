import requests

# Replace this with the Solana address you want to monitor
solana_address = "YOUR_SOLANA_ADDRESS"

def fetch_latest_solana_transactions(address):
    try:
        # Define the Solana RPC endpoint
        solana_rpc_url = "https://api.mainnet-beta.solana.com/"

        # Build the JSON-RPC request
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getConfirmedSignaturesForAddress2",
            "params": [address, {"limit": 10}]  # Adjust the limit as needed
        }

        # Send the request to the Solana RPC endpoint
        response = requests.post(solana_rpc_url, json=payload)

        if response.status_code == 200:
            data = response.json()
            transactions = data.get("result")
            
            if transactions:
                print("Latest Solana transactions for address:", address)
                for tx in transactions:
                    print("Transaction ID:", tx["transaction"]["signature"])
                    print("Block:", tx["slot"])
                    print("Timestamp:", tx["blockTime"])
                    print("--------------------------------------------------")
            else:
                print("No transactions found for address:", address)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    fetch_latest_solana_transactions(solana_address)
