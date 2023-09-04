import requests

# Replace this with the Bitcoin address you want to monitor
bitcoin_address = "YOUR_BITCOIN_ADDRESS"

def fetch_latest_bitcoin_transactions(address):
    try:
        # Define the Bitcoin blockchain explorer API endpoint
        explorer_api_url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"

        # Send a GET request to the blockchain explorer API
        response = requests.get(explorer_api_url)

        if response.status_code == 200:
            data = response.json()
            transactions = data.get("data", {}).get("transactions", [])

            if transactions:
                print("Latest Bitcoin transactions for address:", address)
                for tx in transactions:
                    print("Transaction ID:", tx["hash"])
                    print("Block Height:", tx["block_id"])
                    print("Timestamp:", tx["time"])
                    print("--------------------------------------------------")
            else:
                print("No transactions found for address:", address)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    fetch_latest_bitcoin_transactions(bitcoin_address)
