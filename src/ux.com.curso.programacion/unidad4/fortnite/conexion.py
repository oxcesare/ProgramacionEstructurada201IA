import fortnite_api

# Initialize the client (API key is optional for most endpoints)
client = fortnite_api.FortniteAPI()

# Get current shop items
shop = client.shop.fetch()
for item in shop.featured.items:
    print(f"Item: {item.name} - Price: {item.final_price}")
