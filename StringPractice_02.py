def printInventory(itemsDict, leftWidth, rightWidth):
    print('inventory'.upper().center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
inventoryItems={'Gadget' : 25, 'Widget' : 17, 'Sprocket' : 9, 'Primer' : 7}
printInventory(inventoryItems, 20, 2)
printInventory(inventoryItems, 50, 5)

