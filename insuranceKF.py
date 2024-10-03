'''
   CS5001
   Lab 1
   Fall 2020
   Keavan Farsad
   Car Budget lab problem
'''


INSURANCE = 1600 # insurance is constant

def main():
   
    # Problem 2 - Insurance
    maintenance_cost = 0.005 #per mile 
      

    miles_driven = float(input("How many miles per month do you drive? "))
    average_gas_price = float(input("What is the average price of a gallon of gas? "))
    
    fuel_efficiency = float(input("How many miles per gallon does your car get on average? "))
    
    maintenance_cost = miles_driven * 0.005
    fuel_cost = (miles_driven * average_gas_price) / fuel_efficiency
    monthly_cost = (INSURANCE / 12) + maintenance_cost + fuel_cost
    
    print("Your total expense per month is ${:.2f}".format( monthly_cost))
    

main()
