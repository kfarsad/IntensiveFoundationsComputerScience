
'''
   CS5001
   Lab 1
   Fall 2021
   Keavan Farsad
'''

def main():

    TicketCost = float(7.95)
    DeliveryPopcorn = float(8.95)
    DeliveryDrink = float(4.25)

    LoyaltyDiscount = 0.10

    numberTickets = int(input("How many tickets are you buying? "))
    numberSnacks = int(input("How many buckets of popcorn? "))
    numberDrinks = int(input("How many drinks? "))

    TotalCost = numberTickets * TicketCost + numberSnacks * DeliveryPopcorn + numberDrinks * DeliveryDrink

    print(f"Your price before the discount is ${TotalCost:.2f}")
    print(f"Your price after discount ${TotalCost - TotalCost * LoyaltyDiscount:.2f}")

if __name__ == "__main__":
    main()