'''
    CS 5001 Lab 2
    Fall 2024
    File functionalpractice.py
'''

from menu import menu

def main():
    question = ('How do you like to keep active?\n'
                ' A: Running\n B: Birdwatching\n C: Swimming\n'
                ' D: Does laying on a couch count?\n Your answer: ')
    answer = menu(question)
    print('You selected: ', answer)

main()

