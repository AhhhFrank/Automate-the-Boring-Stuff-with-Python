#! python3
# fantasy_game_inventory_list_to_dict.py
# Arthur: Frank Lee
# Date: 11/27/23
###
# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named addToInventory(inventory, addedItems), 
# where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) 
# and the addedItems parameter is a list like dragonLoot. 
# The addToInventory() function should return a dictionary that represents the updated inventory. 
# Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

# def addToInventory(inventory, addedItems):
#     # your code goes here

# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)

# The previous program (with your displayInventory() function from the previous project) would output the following:

# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger

# Total number of items: 48
###

import sys
import fantasy_game_inventory

# check if loot type is in inv, if yes then add one, if no then use update function. Copy inventory arg to new dict
def addToInventory(inventory, addedItems):
	new_inv = inventory.copy()
	for item in addedItems:
		if item in new_inv.keys():
			new_inv[item] += 1
		else:
			new_inv.update({item: 1})
	return new_inv


def main():
	inv = {'gold coin': 42, 'rope': 1}
	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	inv = addToInventory(inv, dragonLoot)
	fantasy_game_inventory.displayInventory(inv)


if __name__ == '__main__':
	sys.exit(main())
