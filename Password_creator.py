"""by MSKF"""
"""edited by ASHKAN"""

import string # Import and use this instead
from random import choice


# List of avalable words, numbers, symbols
words_list = [x for x in string.ascii_letters]
numbers_list = [x for x in string.digits]
symbols_list = [x for x in string.punctuation]

characters_list = words_list + numbers_list + symbols_list

def program():

    # Get the lenght of password
    try:
        lenght = int(input("Enter the lenght of password: "))

    except ValueError:
        input("** Enter a number!!! **\n")
        # Restart the program
        program()


    # The default password
    password = ''


    # Create the password
    # << use the common way >>
    for x in range(0, lenght):
        password += choice(characters_list)


    # Print the password
    print(password)


    # Exit the program
    input("Exit> ")


# Start the program
program()