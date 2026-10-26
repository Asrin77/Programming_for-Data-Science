#exercise 8

products = [
    {"name": "Jiji", "price": 920, "quantity": 3},
    {"name": "key chains", "price": 200, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Hello kitty", "price": 650, "quantity": 1}
    ]

price = []
quantity = []
names = []
for add in products:
    price.append(add["price"])
    quantity.append(add["quantity"])
    names.append(add["name"])

def calculating(price, quantity, names):
    total_prices = 0
    highest = 0
    product_name = ""

    for x in range(len(price)):
        total = price[x] * quantity[x]
        total_prices += total
        print(f"{names[x]}: {total}")

        if total > highest:
            highest = total
            product_name = names[x]

    return total_prices, highest, product_name

total_prices, highest, product_name = calculating(price, quantity, names)

print("Total inventory value:", total_prices)
print("Highest line total:", product_name, highest)

    