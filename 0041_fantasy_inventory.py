#You are creating a fantasy game. Task is to build a function that search for inventory

inventory = {'lina': 1, "pochodnia": 6, 'złote monety': 42, 'sztylet': 1, 'strzała': 12}
dragonLoot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'rubin']

def displayInventory(inventory):
    print("Inwentarz: ")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Całkowita liczba przedmiotów: " + str(item_total))

def addToInventory(inv, addedItems):
    for item in addedItems:
        if item in inv:
            inv[item] += 1
        else:
            inv.setdefault(item, 1)

addToInventory(inventory, dragonLoot)
displayInventory(inventory)
