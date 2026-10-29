products = [
    ("P101", 25.50, 12),
    ("P102", 10.00, 3),
    ("P103", 45.00, 0),
    ("P104", 8.50, 7)
]

total_value = 0

for product_id, price, stock in products:
    value = price * stock
    total_value += value

    print("Product:", product_id)
    print("Inventory value:", value)

    if stock < 5:
        print("Low stock! Reorder required")

print("Total inventory value:", total_value)