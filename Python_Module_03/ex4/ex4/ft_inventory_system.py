import sys

print("=== Inventory System ===")

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
        print(f"Quantity error for '{parts[0]}': {e}")
        continue
    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        continue
    inventory[item_name] = quantity

print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")
print(f"Total quantity of "
      f"the {len(inventory.keys())} items: {sum(inventory.values())}")
total = sum(inventory.values())
for item, qty in inventory.items():
    percent = qty / total * 100
    print(f"Item {item} represents {percent:.1f}%")
most = max(inventory, key=lambda k: inventory[k])
least = min(inventory, key=lambda k: inventory[k])
print(f"Item most abundant: {most} with quantity {inventory[most]}")
print(f"Item least abundant: {least} with quantity {inventory[least]}")
inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
