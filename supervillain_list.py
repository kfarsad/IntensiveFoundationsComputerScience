'''
    CS 5001
    PP5: More fun with lists and loops
'''
# Villain roster.
# NB: Joker's first name is Jack. Last name?? Jack? Not a typo here

VILLAINS = [['Von Doom', 'Victor'], ['Octavius', 'Otto'], ['Luthor', 'Lex'],
            ['Dent', 'Harvey'], ['Fisk', 'Wilson'], ['Jack', 'Jack']]
    

def main():
    villain_roster = []
    print('Party List of super villains start is: ', VILLAINS)
    print('+++' * 5)
    
    # swap first and last names in our villain list - conceptual operations
    # old fashioned way
    # work with the list of lists here. remember to work with a copy,
    # so EACH of the sub-lists must use the copy() method
    for each in VILLAINS:
        each_copy = each.copy()
        temp = each_copy[0]
        each_copy[0] = each_copy[1]
        each_copy[1] = temp
        villain_roster.append(each_copy)
        
    print('Party List after swapping firstname/lastname is: ', villain_roster)
    print('---' * 5)
    
    # prove to ourselves that we're modifying our copy, NOT the original
    # villains list
    print('Original Party List VILLAINS is: ', VILLAINS)

    print('+++' * 5)

main()
