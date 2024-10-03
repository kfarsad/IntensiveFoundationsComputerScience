'''
    CS 5001 Lab 2
    Fall 2020
    functionalPracticePart2.py
'''

from menu import menu

def main():
    # First question
    question1 = ('How do you like to keep active?\n'
                 ' A: Running\n B: Birdwatching\n C: Swimming\n'
                 ' D: Does laying on a couch count?\n Your answer: ')
    answer1 = menu(question1)
    print('You selected: ', answer1)

    # Second question
    question2 = ('What is your favorite food?\n'
                 ' A: Salad\n B: Cakes and Pies\n C: Sandwiches\n D: Yes\n Your answer: ')
    answer2 = menu(question2)
    print('You selected: ', answer2)

    # Third question
    question3 = ('What grade do you want to get in CS 5001?\n'
                 ' A: A\n B: A\n C: A\n D: Is this a real question?\n Your answer: ')
    answer3 = menu(question3)
    print('You selected: ', answer3)

main()
