"""Functions to keep track and alter inventory."""


def create_inventory(items: list, inventory: dict=None) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    if inventory == None:
        inventory = {}
    else:
        for item, qtd in inventory.items():
            for x in range(qtd):
                items.append(item)
    
    for item in items:
        inventory[f'{item}'] = items.count(item)
    return inventory

def add_items(inventory, items) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    return create_inventory(items=items, inventory=inventory)

def decrement_items(inventory, items) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if inventory[item] == 0:
            continue
        else: inventory[item] = inventory[item] - 1
    return inventory


def remove_item(inventory: dict, item) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    
    try: inventory[item]
    except KeyError:
        return inventory
    del inventory[item]
    return inventory

def list_inventory(inventory: dict) -> list:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = [(item, qtd) for item, qtd in inventory.items() if qtd > 0]
    inventory_list.sort()

    return inventory_list
