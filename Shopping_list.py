"""by MSKF"""
"""edited by ASHKAN"""


# The list
shopping_list = []


# Helps
def show_help():
    # advise -> when you've defined your string using "" (double qouts)
    # you can also use '' (single qouts) within your string witout getting error
    print("You can add items.") 
    print("Enter 'DONE' to finish adding.")
    print("Enter 'HELP' to show help.")
    print("Enter 'SHOW' to see your list.")
    print("Enter 'REMOVE' to remove an item.")


# Show the list
def show_list():
    print("Here\'s your list: ")

    # there is a better way to print the numbers
    # use enumerate function of python instead

    for num, item in enumerate(shopping_list):
        print("{num}. {item}" .format(num = num+1, item = item))
        num += 1


# Add an item to the list
def add_to_list(x):

    # instead of this complicated code
    # use this syntax if you wanna check weather an item
    # exists in a list or not
    if x.lower() in shopping_list:
        print("Its added before.")

    else:
        shopping_list.append(x.lower())
        print("{item} added to list.\n Your list has {num} items now.".format(item = x, num = len(shopping_list)))


# Remove an item to the list
def remove_from_list(z):
    z = input("What do you want to remove? ")

    if z.lower() in shopping_list:
        shopping_list.remove(z.lower())
        print("{item} removed from list.\n Your list has {num} items now.".format(item = z, num = len(shopping_list)))

    else:
        print("{item} isn\'t in your list!!!".format(item = z))


# Program
def run_app():

    # Show the help
    show_help()


    # Check the answer
    while True:
        x = input("> ")


        # If done
        if x.upper() == "DONE":
            show_list()
            break

        # If help
        elif x.upper() == "HELP":
            show_help()
            continue

        # If show
        elif x.upper() == "SHOW":
            show_list()
            continue

        # If remove
        elif x.upper() == "REMOVE":
            remove_from_list(x)
            continue

        # Else
        else:
            add_to_list(x)


# Start the program
run_app()