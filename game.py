"""A number-guessing game."""

# Put your code here
import random
from os import sep

greeting = 'Hello!'
print(greeting)

user_name = input('What is your name?\n')
print("Nice to meet you", ' ', user_name, '.', sep='')

def random_number_generator ():
    rand_number = random.randint(1, 100)
    # print(rand_number)
    user_guess = int(input('Please guess a number between 1-100.\n'))
    while rand_number != 'user_guess':
        if user_guess > 100 or user_guess < 1:
            user_guess = int(input('Please guess a number within your IQ range of 1-100.\n'))
        elif user_guess >  rand_number:
            print("That is too high")
            user_guess = int(input('Please guess a number between 1-100.\n')) #without this it will go into an infinite loop of print
        elif user_guess < rand_number:
            print("That is too low")
            user_guess = int(input('Please guess a number between 1-100.\n'))
        else:
            print('Wow you got it,', user_name, 'is so smart!')
            break     

random_number_generator()