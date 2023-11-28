#! python3
# Arthur: Frank Lee
# Date: 11/28/23
# idiot.py
###
# Let’s use PyInputPlus to create a simple program that does the following:
# Ask the user if they’d like to know how to keep an idiot busy for hours.
# If the user answers no, quit.
# If the user answers yes, go to Step 1.
# (This is a follow along problem with the solution written out in the book)
###

import pyinputplus as pyip


while True:
	prompt = 'Want to know how to keep an idiot busy for hours?\n'
	response = pyip.inputYesNo(prompt)
	if response == 'no':
		print('Thank you. Have a nice day.')
		break
