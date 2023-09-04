import requests

# Replace this with the Dogecoin address you want to monitor
dogecoin_address = "YOUR_DOGECOIN_ADDRESS"

def fetch_latest_dogecoin_transactions(address):
    try:
        # Define the Dogecoin blockchain explorer API endpoint
        explorer_api_url = f"https://dogechain.info/api/v1/address/{address}"

        # Send a GET request to the Dogecoin blockchain explorer API
        response = requests.get(explorer_api_url)

        if response.status_code == 200:
            data = response.json()
            transactions = data.get("transactions", [])

            if transactions:
                print("Latest Dogecoin transactions for address:", address)
                for tx in transactions:
                    print("Transaction Hash:", tx["txid"])
                    print("Amount:", tx["amount"])
                    print("Block Height:", tx["block"])
                    print("Timestamp:", tx["time"])
                    print("--------------------------------------------------")
            else:
                print("No transactions found for address:", address)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    fetch_latest_dogecoin_transactions(dogecoin_address)
