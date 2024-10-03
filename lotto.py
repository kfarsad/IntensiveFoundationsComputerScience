'''
    CS5001
    Spring 2020
    Lab 3
    Guess My Number
    Write the code to play the guess my number game
    
'''

import random

MAX_GUESSES = 5


def main():
    number = random.randint(1, 5)
    player_name = input('Hello! What is your name? ')
    print('Cool! Great to meet you, ' + player_name + '. Let\'s play!')
    print('I\'m thinking of a number between 1 and 5.')

    guess = int(input('Enter your guess '))
    if guess == number:
        print('Yay! You guessed my number!')
    elif guess < number:
        print('Sorry...your guess was too low.')
        print('My number was: {}'.format (number))        
    elif guess > number:
        print('Unfortunately, your guess was too high.')
        print('My number was: {}'.format (number))

main()
