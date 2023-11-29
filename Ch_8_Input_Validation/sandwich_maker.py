#! python3
# Arthur: Frank Lee
# Date: 11/28/2023
# sandwich_maker.py
###
# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
# Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
###

import pyinputplus as pyip 
import sys

# write functions to take preference for each ingredients and return choices
# write function to calculate cost
# write function to output the whole sandwich(es) and cost


def bread_type():
	bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='What type of bread would you like?\n')
	return bread


def protein_type():
	protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='What kind of protein would you like?\n')
	return protein


def cheese():
	cheese = pyip.inputYesNo(prompt='Do you want cheese?\n')
	if cheese == 'yes':
		cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt='What kind of cheese would you like?\n')
	return cheese


def condiment_and_toppings():
	extras = ['mayo', 'mustard', 'lettuce', 'tomato']
	order = []
	for stuff in extras:
		if pyip.inputYesNo(prompt='Do you want %s?\n' % (stuff)) == 'yes':
			order.append(stuff)
	return order


def number_of_sandwhich():
	sando = pyip.inputInt(prompt='How many sandwhiches do you want?\n', min=1)
	return sando


def cost(bread, protein, cheese, extras, sandos):
	ingredient_cost = {'wheat': 1.0, 'white': 0.5, 'sourdough': 1.5,
						'chicken': 1.0, 'turkey': 0.75, 'ham': 1.25, 'tofu': 1.0,
						'cheddar': 0.5, 'swiss': 0.5, 'mozzarella': 0.5,
						'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.25, 'tomato': 0.75}


def main():
	#print(bread_type())
	#print(protein_type())
	#print(cheese())
	#print(condiment_and_toppings())
	print(number_of_sandwhich())


if __name__ == '__main__':
	sys.exit(main())
