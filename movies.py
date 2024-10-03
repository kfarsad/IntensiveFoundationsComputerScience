'''
    CS 5001
    Fall 2020
    Keith
    Movie Tickets
    Calculate the total cost for taking your friends to see a movie
    Including popcorn, tickets, drinks
'''

# define our global variables

TICKET_COST = 7.95
POPCORN_COST = 8.95
DRINK_COST = 4.25

def main():
    tickets = int(input('How many tickets do you want? '))
    popcorn = int(input('How many buckets of popcorn? '))
    drinks = int(input('How many drinks? '))

    total_cost = (  (tickets * TICKET_COST) + 
                    (popcorn * POPCORN_COST) + 
                    (drinks * DRINK_COST))

    # check our work
    print('Total cost is ${:.2f}'.format(total_cost))
    # discount = round((total_cost * 0.1), 2) # calculate discount
    
    total_cost = total_cost - (total_cost * 0.1) # apply discount
    print('Your price after the discount is: ${:.2f}'.format(total_cost))


main()
