customers = {"name": "Cecep", "age": 30, "address": "Subang"}

customers["company"] = "Redcomm"
customers["name"] = "Joko"

print(customers["name"])
print(customers["age"])
print(customers["address"])

del customers["address"]

for key, value in customers.items():
    print(f"{key}: {value}")
