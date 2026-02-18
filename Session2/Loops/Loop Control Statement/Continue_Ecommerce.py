products = ["Shoes", "T-shirt", "Laptop", "Watch"]
out_of_stock = ["Laptop"]

for item in products:
    if item in out_of_stock:
        continue   # Skip this product
    print("Available:", item)
