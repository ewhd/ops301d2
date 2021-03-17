#!/user/bin/env python3

# Script:                       challenge311-file-handling.py
# Author:                       Ethan Denny
# Date of latest revision:      3/15/2021
# Purpose:     This script creates a .txt file, appends three lines, 
#              prints the first line, then deletes the file.

# Resource: https://www.w3schools.com/python/python_file_handling.asp
#           https://www.w3schools.com/python/python_file_write.asp
#           https://www.w3schools.com/python/python_file_remove.asp

import os


# Main

# This section creates the file and prepares it to be appended to,
# appends three lines, then closes the file
file_to_append = open("demo.txt", "a")
file_to_append.write("blah\nblah\nblah")
file_to_append.close()

# This line opens the file again and prepares it to be read, prints 
# the first line, then closes the file
file_to_read = open("demo.txt", "r")
print(file_to_read.readline())
file_to_read.close()

# This line deletes the file
os.remove("demo.txt")


# End
