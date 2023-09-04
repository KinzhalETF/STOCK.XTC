import requests

# Define the URL of the website's endpoint where you want to submit the POST request
url = "https://example.com/submit"

# Define the data you want to submit in the POST request (in this example, a simple form)
data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "message": "Hello, this is a test message."
}

# Send the POST request with the data
response = requests.post(url, data=data)

# Check the response from the server
if response.status_code == 200:
    print("POST request successful!")
    print("Response from server:")
    print(response.text)
else:
    print("POST request failed with status code:", response.status_code)
