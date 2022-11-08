import requests
address="LjGAwuNINRJaraC0W7OBdU4fBL9beJvwgGW7jq2FVtZtXb0G5lMl4aZ0VYnPDUif"
url = "https://solana-gateway.moralis.io/nft/mainnet/"+address+"/metadata"
headers = {
    "accept": "application/json",
    "X-API-Key": "LjGAwuNINRJaraC0W7OBdU4fBL9beJvwgGW7jq2FVtZtXb0G5lMl4aZ0VYnPDUif"
}
response = requests.get(url, headers=headers)
print(response.text)