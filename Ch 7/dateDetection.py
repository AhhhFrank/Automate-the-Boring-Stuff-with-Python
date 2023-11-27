#! python3
# dateDetection.py
# Arthur: Frank Lee
# Date: 11/22/23
#####
# Write a regular expression that can detect dates in the DD/MM/YYYY format. 
# Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. 
# Note that if the day or month is a single digit, it’ll have a leading zero.
# 
# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. 
# Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. 
# April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. 
# February has 29 days in leap years. 
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 
# Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
#####

import re
import sys

#gets date and returns month, day, and year value
def getDate(date):
	dateRegex = re.compile(r'''
		(0[1-9]|[12][0-9]|3[01])		# day from 01-31
		(/)								# separator
		(0[1-9]|1[12])					# month from 01-12
		(/)								# separator
		([12][0-9]{3})					# year from 1000-2999
		''', re.VERBOSE)
	mo = dateRegex.search(date)
	return mo.group(1), mo.group(3), mo.group(5)


# Check if leap year, returns True if leap year else False. 
def checkYear(year):
	year = int(year)
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		return True
	return False


# TODO Check if correct days in month
def checkMonth(day, month, year):
	day = int(day)
	day30 = ['04', '06', '09', '11']
	if month in day30:					# check if month with 30 days
		if day <= 30:
			return True
		return False
	elif month == '02':					# check feb and leap year
		if checkYear(year):
			if day <= 29:
				return True
		elif day <= 28:
			return True
		return False
	else:								# check rest of months and 31 days
		if day <= 31:
			return True
		return False


def dateDetection():
	while True:
		print('Enter Date in DD/MM/YYYY format (or blank to exit): ')
		date = input()
		if date == '':
			break
		day, month, year = getDate(date)
		if checkMonth(day, month, year):
			print('This is a valid date')
		else:
			print('This is NOT a valid date')


def main():
	dateDetection()


if __name__ == '__main__':
	sys.exit(main())  # noqa: W292