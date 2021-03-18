#!/user/bin/env python3

# Script:                       challenge313-request-library.py
# Author:                       Ethan Denny
# Date of latest revision:      3/17/2021
# Purpose:          This script performs an HTTP request on a given url 
#                   and returns status and header information.

# Description:
# This script prompts the user for a URL, then saves that as a string to a variable.
# Then it prompts the user for an HTTP method.
# Then the script repeats back what it is about to do (perform X HTTP method on Y URL)
# and asks the user for confirmation.
# Then it uses the requests library to perform the operation.
# Then it translates the response code into human language and pritns it, along with
# response header iformation.

# References:
# https://docs.python.org/3/library/functions.html#getattr

import requests, sys, validators


# Define Variables

# This variable will hold the url received from the user
target_url_var = str

# This variable will hold the HTTP method chosen by the user
http_method_var = int

# This variable will hold the output of calling the `requests` module
response = None

# This variable holds a list of HTTP methods
http_method_list = ("get", "post", "put", "delete", "head", "patch", "options")



# Define Functions

# This is a function to prompt a user for yes or no (y/n) and return True or False.
# I pulled it from here: https://gist.github.com/garrettdreyfus/8153571#gistcomment-3519679
def yesno(question):
    """Simple Yes/No Function."""
    prompt = f'{question} ? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print(f'{ans} is invalid, please try again...')
        return yesno(question)
    if ans == 'y':
        return True
    return False


def Main():
    proceed = False
    url_valid = False
    option_valid = False

    # This while loop gets inputs from the user and confirms that the inputs are valid
    while proceed == False:
        # This section prompts the user for a url, then checks that it is valid. If the url is
        # is valid it continues, and if not it loops until it is
        # See: https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/
        # while url_valid == False:
        #     target_url_var = input("Enter a valid URL:\n")
        #     if validators.url(target_url_var) == True:
        #         break
        #     print("That is not a valid URL. Please try again.\n(Hint: did you begin with http://?)")

        # This section gives the user options of different HTTP methods (and an option to exit)
        print("\nPlease select an HTTP Method from the follwoing options: \n\
            1. GET\n\
            2. POST\n\
            3. PUT\n\
            4. DELETE\n\
            5. HEAD\n\
            6. PATCH\n\
            7. OPTIONS\n\
            8. Exit Program\n\
            ")

        # This section requests the user to choose one of the options given. It runs until a valid option is selected.
        while True:
            try:
                http_method_var = int(input("Enter the number (1-8) of the option you wish to use: "))
                if 1 <= http_method_var <= 8:
                    break
            except:
                print("That's not a number! Please try again")

        # This section first checks if the user selected the option to exit the program. If so then the program ends.
        # If not then it prints what the program will do next and asks the user to confirm
        if http_method_var == 8:
            sys.exit("Goodbye!")
        else:
            print("This script is about to perform a X request on Y url.")
            proceed = yesno("Would you like to proceed")
    
    target_url_var = "http://google.com"
    

    # This section uses getattr to call the module `requests` and uses the value of http_method_var with http_methods_list 
    # to call the correct method. It stores the output in a variable
    response = getattr(requests, http_method_list[http_method_var - 1])(target_url_var)
    print(response)

    




# Main
Main()

# End