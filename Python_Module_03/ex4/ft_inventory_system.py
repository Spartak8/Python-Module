import sys

print("=== Inventory System Analysis ===")

inventory = {}

for args in sys.argv[1:]:
    parts = args.split(":")

    if len(parts) != 2:
        print(f"Error - invalid parameter '{args}'")
        continue

    item_name = parts[0]
    try:
        quantity = int(parts[1])
    except ValueError as e:
        print(f"Quantity error for {parts[0]}: {e}")
        continue
    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        continue
    inventory[item_name] = quantity

print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")
print(f"Total quantity of the {len(inventory.keys())} items: {sum(inventory.values())}")



