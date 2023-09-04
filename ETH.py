import requests

# Replace this with the Ethereum address you want to monitor
ethereum_address = "YOUR_ETHEREUM_ADDRESS"

def fetch_latest_ethereum_transactions(address):
    try:
        # Define the Ethereum blockchain explorer API endpoint
        explorer_api_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc"

        # Replace with your own Etherscan API key (sign up for a free API key on etherscan.io)
        api_key = "YOUR_ETHERSCAN_API_KEY"

        # Send a GET request to the Ethereum blockchain explorer API
        response = requests.get(explorer_api_url, params={"apikey": api_key})

        if response.status_code == 200:
            data = response.json()
            transactions = data.get("result", [])

            if transactions:
                print("Latest Ethereum transactions for address:", address)
                for tx in transactions:
                    print("Transaction Hash:", tx["hash"])
                    print("Block Number:", tx["blockNumber"])
                    print("Timestamp:", tx["timeStamp"])
                    print("--------------------------------------------------")
            else:
                print("No transactions found for address:", address)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    fetch_latest_ethereum_transactions(ethereum_address)
