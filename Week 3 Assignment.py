# Lesson 3 Individual Assignment
# Inventory Management System

# Task 1: Create Inventory Dictionary

inventory = {
    "Widget": 10,
    "Gadget": 5,
    "Sensor": 0,
    "Cable": 15
}

# Create the order queue as a list of lists
orders = [
    ["Widget", 3],       # Full fulfillment
    ["Gadget", 7],       # Partial fulfillment
    ["Sensor", 2],       # Out of stock
    ["Cable", 10],       # Full fulfillment
    ["Keyboard", 4],     # Invalid item
    ["Cable", 8],        # Partial fulfillment
    ["Widget", 7]        # Full fulfillment
]

# List to store items and quantities that could not be fully supplied
unfulfilled_orders = []

# Counter for fully fulfilled orders
fully_fulfilled_orders = 0


# Task 2: Process each order

for order in orders:

    item = order[0]
    requested_quantity = order[1]

    # Check whether the item exists in inventory
    stock = inventory.get(item)

    # Case 1: Invalid / Missing Item
    if stock is None:

        print("INVALID ITEM:", item, "- Item does not exist in inventory.")

        unfulfilled_orders.append([item, requested_quantity])

    # Case 2: Out of Stock
    elif stock == 0:

        print("OUT OF STOCK:", item, "- Requested:", requested_quantity)

        unfulfilled_orders.append([item, requested_quantity])

    # Case 3: Full Fulfillment
    elif stock >= requested_quantity:

        inventory[item] = stock - requested_quantity

        fully_fulfilled_orders = fully_fulfilled_orders + 1

        print(
            "FULLY FULFILLED:",
            item,
            "| Requested:", requested_quantity,
            "| Supplied:", requested_quantity,
            "| Remaining Stock:", inventory[item]
        )

    # Case 4: Partial Fulfillment
    elif stock > 0 and stock < requested_quantity:

        supplied_quantity = stock
        unfulfilled_quantity = requested_quantity - supplied_quantity

        inventory[item] = 0

        unfulfilled_orders.append([item, unfulfilled_quantity])

        print(
            "PARTIALLY FULFILLED:",
            item,
            "| Requested:", requested_quantity,
            "| Supplied:", supplied_quantity,
            "| Unfulfilled:", unfulfilled_quantity,
            "| Remaining Stock:", inventory[item]
        )


# Task 3: Final Summary

print("\n========== FINAL SUMMARY ==========")

# 1. Final updated inventory
print("Final Inventory:", inventory)

# 2. Total count of fully fulfilled orders
print("Total Fully Fulfilled Orders:", fully_fulfilled_orders)

# 3. Items and quantities that could not be fully supplied
print("Unfulfilled Orders:", unfulfilled_orders)