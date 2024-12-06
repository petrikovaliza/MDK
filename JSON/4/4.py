import json

with open('products.json', 'r') as json_file:
    data = json.load(json_file)
    
for product in data["products"]:
    if product['price'] > 100:
        print(product['name'])