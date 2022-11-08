import requests
url = "https://solana-gateway.moralis.io/nft/mainnet/2camF6sXuq4eQ2h2815xiA2r3BvoYNQbFztbLNymiwsq/metadata"
headers = {
    "accept": "application/json",
    "X-API-Key": "z1SWBbYXT9C5u4QlvAAqxr6q2WIgJWbClpY9o2ESQfdSKOA4VRxTm9WoZmH2Zrnj"
}
response = requests.get(url, headers=headers)
print(response.text)
