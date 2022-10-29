from dicts import create_inventory, add_items, decrement_items, remove_item, list_inventory

print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))