# Exercise 3: Guess the Number Game

# Write a Python program for a game that randomly generates a number between 
# 1 and 100 and asks the user to guess the number. The program should tell the 
# user if their guess is too high, too low, or correct. This will help you 
# understand how to use conditionals and loops in Python, and also how to generate 
# random numbers. For an extra challenge, limit the number of guesses the user can
# make.

import random

random_number = random.randint(1, 10)
guess_num_limit = 5
while guess_num_limit > 0:
    print('Guess the number:')
    guess = int(input())
    guess_num_limit = guess_num_limit - 1
    if (guess < random_number):
        print('Your guess is low')
    elif (guess > random_number):
        print('Your guess is high')
    else:
        print('You got it right')
        break
