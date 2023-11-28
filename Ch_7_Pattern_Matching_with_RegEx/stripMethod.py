#! python3
# stripMethod.py
# Arthur: Frank Lee
# Date: 11/21/23
###
# Write a function that takes a string and does the same thing as the strip() string method. 
# If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 
# Otherwise, the characters specified in the second argument to the function will be removed from the string.
###

import sys
import re

#TODO function with optional arg
#TODO then replace with regex to strip

def stripMethod(text, strip= ''):
	print(text + '1')
	if strip == '':
		mo = re.sub(r'^\s+|\s+$', '', text)
	else:
		mo = re.sub(format(strip), '', text)
	print(mo + '1')


def main():
	stripMethod(' spameggspameggsapmeegg ', 'egg')


if __name__ == '__main__':
	sys.exit(main())