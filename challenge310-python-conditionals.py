#!/user/bin/env python3

# Script:                       challenge310-python-conditionals.py
# Author:                       Ethan Denny
# Date of latest revision:      3/12/2021
# Purpose:     Demonstrate the use of various conditional statements


# Define Variables
a = "a"
b = 1


# This section determines if a and b are equal or not equal
if a == b:
    print("a equals b")
elif a != b:
    print("a does not equal b")


# This section returns true statements about the relationship between integers a and b
if type(a) != int and type(b) != int:
    print("niether a nor b are integers")
elif type(a) != int or type(b) != int:
    print("either a or b are not integers")
elif a <= b:
    print("a is less than or equal to b")
    if a < b:
        print("a is less than b")
elif a >= b:
    print("a is greater than or equal to b")
    if a > b:
        print("a is greater than b")
else:
    pass


# End
