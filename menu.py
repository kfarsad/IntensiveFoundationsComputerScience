'''
    CS 5001 Lab 2
    Fall 2024
    File menu.py
'''

# Define the menu function
def menu(question):
    '''
    input: Selecting answer for the question and providing a capitalized response.

    output: A, a, B, b, C, c, D, d, ... etc.

    # Test Case 1: Input 'a' -> expected output: 'A'
    # Test Case 2: Input 'b' -> expected output: 'B'
    # Test Case 3: Input 'C' -> expected output: 'C'
    '''
    # Display the question and get input from the user
    answer = input(question).strip()  # Strip whitespace
    return answer.upper()  # Transform input to uppercase

    main()

