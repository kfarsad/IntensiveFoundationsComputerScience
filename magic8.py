'''
    Lab 4
    Magic 8 Ball
    Some of us "old tymers" had this toy as a kid. It's pretty dumb, my 7-year
    old self thought it was amazing. And it passed the time on those long
    car rides since we didn't have "We Fee" (WiFi), CDs, DVDs or mobile
    electronic gadgets

    Goal: More practice accessing and using lists. Accept user input,
    answer a random saying from the original toy 8-ball list

    Optional Goal: Practice with command-line arguments and sys.argv.
    Allow for user to ask a one-shot question and get a witty response
    before exiting the program
'''

import random
import sys

RESPONSES = ['As I see it, yes.', ' Ask again later.', 'Better not tell you now.',
            'Cannot predict now.','Concentrate and ask again.',
            'Don’t count on it.', 'It is certain.',
            'It is decidedly so.','Most likely.', 'My reply is no.',
            'My sources say no.', 'Outlook not so good.',
            'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.',
            'Very doubtful.', 'Without a doubt.', 'Yes.',
            'Yes – definitely.', 'You may rely on it.']
 

def main():
    random.seed() # seed our psuedo-random number generator

    # this section is for part 2 of question 1. If command line is used
    # return one random saying and quit the program

    if len(sys.argv) > 1: # command-line invocation with arguments
        print(random.choice(RESPONSES))
    else:  # Interactive invocation (no arguments). Loop until :q:
        print('Welcome to Magic 8 Ball.')
        print('Enter your question, and I will prognosticate an answer for you!')

        while True:
            question = input('What is your question (:q: to quit)? ')
            if question.lower() == ':q:':
                break

            # select a random item from our list of responses
            answer = random.choice(RESPONSES)

            # NB:the following commented code would work the same as the above
            # index = random.randint(0, len(RESPONSES) - 1)
            # answer = RESPONSES[ index ]
            
            print(answer + '\n' + '---' * 5)
        
    print('My wise sayings will now cease')

    
main()
