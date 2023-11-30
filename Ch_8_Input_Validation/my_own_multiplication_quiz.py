#! python3
# Arthur: Frank Lee
# Date: 11/29/2023
# my_own_multiplcation_quiz.py
###
# To see how much PyInputPlus is doing for you, try re-creating the multiplication 
# quiz project on your own without importing it. 
# This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. 
# You’ll need to implement the following features:
# If the user enters the correct answer, the program displays 
# “Correct!” for 1 second and moves on to the next question.
# The user gets three tries to enter the correct answer 
# before the program moves on to the next question.
# Eight seconds after first displaying the question, the question is 
# marked as incorrect even if the user enters the correct answer after the 8-second limit.
###
import sys
import time
import random


# create 10 multiplication problems from 0x0 to 9x9 for the user
#	use random to gen 2 numbers between 0-9 and multiple for answer and for loop 10 times
# check if the user answered it correctly, if correct add to total and move after 1 second. If not give 2 more tries
#	put into a loop for 3 times, if correct break the loop (after a second and correct message and add to total), if after 3 incorrect, move on
# make user have 3 tries to get correct answer per problem
# give user 8 seconds total to answer each problem 
#	idk how to do this... use int(time.time()) to calcuate 8 seconds (question start to answer and see if it's 8 seconds)


def num_gen():
	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)
	answer = num1 * num2
	return num1, num2, str(answer)


def multi_problem():
	total_correct = 0
	total_questions = 10
	tries = 3
	for question in range(total_questions):				# loop total_questions (10) times for number of questions asked
		num1, num2, answer = num_gen()
		print('%s: %s * %s = ' % (question, num1, num2))
		start_time = int(time.time())					# record starting time 		
		for user_try in range(tries):					# loop tries (3) times, for number of times a user has to guess
			user_answer = str(input())					
			if int(time.time()) - start_time > 8:		# checks if 8 seconds has elapsed since the question has been asked, is so break
				print('Out of time!')
				break
			elif user_answer == answer:					# if the answer is correct, add to total and sleep for 1second
				total_correct += 1
				print('Correct!')
				time.sleep(1)
				break
			elif user_try == 2:							# if on last try then print last try
				print('Out of tries!')
			else:
				print('%s: %s * %s = ' % (question, num1, num2))
	print('%s out of %s correct!' % (total_correct, total_questions))


def main():
	multi_problem()


if __name__ == '__main__':
	sys.exit(main())
