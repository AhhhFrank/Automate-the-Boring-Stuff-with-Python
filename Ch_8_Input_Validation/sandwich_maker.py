#! python3
# Arthur: Frank Lee
# Date: 11/28/2023
# sandwich_maker.py
###
# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
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
	bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='What type of bread do you want?\n')
	return bread


def protein_type():
	protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='What kind of protein do you want?\n')
	return protein


def cheese():
	cheese = pyip.inputYesNo(prompt='Do you want cheese?\n')
	return cheese


def main():
	print(bread_type())
	print(protein_type())
	print(cheese())


if __name__ == '__main__':
	sys.exit(main())
