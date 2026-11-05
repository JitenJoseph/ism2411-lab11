# Self-Assessment Questions
# 1. I would use .get() if there was a chance that the key is not present in the dictionary. For example if there is an optional email address. Whereas I would use [] if I knew the key would be present. This would cause an error if it wasn’t.
# 2. Exercise 8 reminds me using Excel to work out the total sales across certain regions. However, Python would be more useful for larger data sets as you can automatically work out totals.


# Exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and add
customer["phone"] = "555-0101"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email is not in the dictionary")


# Exercise 4: Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the keys,
# instead of both the keys and values.
for key in customer:
    print(key)


# Exercise 5: Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", tier)
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of dictionaries
customer2 = {
    "name": "Bob",
    "email": "bob@example.com",
    "tier": "silver",
    "ytd_spend": 500
}

customer3 = {
    "name": "Carla",
    "email": "carla@example.com",
    "tier": "bronze",
    "ytd_spend": 150
}

customers = [customer, customer2, customer3]

for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{person['name']} - {tier} - ${discount_amount:.2f} discount")


# Exercise 7: Nested catalog
catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} ({details['stock']} remaining)")


# Exercise 8: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

regional_sales = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    regional_sales[region] = regional_sales.get(region, 0) + amount

for region in sorted(regional_sales):
    print(f"{region}: {regional_sales[region]}")
