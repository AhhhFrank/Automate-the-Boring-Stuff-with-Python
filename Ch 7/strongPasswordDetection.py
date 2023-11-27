#! python3
# trongPasswordDetection.py
# Arthur: Frank Lee
# Date: 11/20/23

###
# Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. 
# You may need to test the string against multiple regex patterns to validate its strength.
###

import sys
import re

#TODO make sure pw at least 8 chars
def checkPassLength(password):
	if len(password) >= 8:
		return True
	return False


#TODO check pw to include at least 1 upper, 1 lower, and 1 digit
def checkUpper(password):
	upperRegex = re.compile(r'[A-Z]')
	mo = upperRegex.search(password)
	if mo == None:
		return False
	return True

def checklLower(password):
	lowerRegex = re.compile(r'[a-z]')
	mo = lowerRegex.search(password)
	if mo == None:
		return False
	return True

def checkNum(password):
	numRegex = re.compile(r'\d')
	mo = numRegex.search(password)
	if mo == None:
		return False
	return True

def checkPassword():
	while True:
		print('Enter password to check strength(or blank to exit): ')
		password = input()
		if password == '':
			break
		if checkPassLength(password) and checkUpper(password) and checklLower(password) and checkNum(password):
			print('Good Password')
		else:
			print('Weak')


def main():
	checkPassword()


if __name__ == '__main__':
	sys.exit(main())