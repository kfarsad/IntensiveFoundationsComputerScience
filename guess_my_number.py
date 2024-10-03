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
    number = random.randint(1, 100)
    player_name = input('Hello! What is your name? ')
    print('Cool! Great to meet you, ' + player_name + '. Let\'s play!')
    print('I\'m thinking of a number between 1 and 100.')
    print('You have ', MAX_GUESSES, ' guesses.')

    num_guesses = 0
    found = False
    while num_guesses < MAX_GUESSES and not found:
        num_guesses = num_guesses + 1 
        guess = int(input('Enter your guess '))
        if guess == number:
            print('Yay! You guessed my number!')
            found = True
        elif guess < number:
            print('Nope.Too low.')
        elif guess > number:
            print('Nah. Too high.')
    if found:
        print('Great job! You won in ', num_guesses, ' tries')
    else:
        print('Nice try, but you lost this time. My number was: {}'.format (number))

main()
