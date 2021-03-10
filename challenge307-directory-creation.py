#!/user/bin/env python3

# Script:                       challenge307-directory-creation.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/9/2021
# Purpose:     
#           This script generates all directories, sub-directories and files for a 
#           user-provided directory path.


# Import libraries

import os
import sys

# Declaration of variables

# This line takes a path input from the user
path_var = input("Enter path: ")


# Declaration of functions

# This function takes a path and performs os.walk() on it for the root, directories,
# and files
def bash_walk(path):
    for (root, dirs, files) in os.walk(path):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)



# Main

# This section opens a new file, calls the function with path_var as the argument,
# then closes the file
sys.stdout = open("walk_output.txt", "w")
bash_walk(path_var)
sys.stdout.close()

# This section opens the file in Nano (because I can't test running it in LibreOffice!)
os.system("nano walk_output.txt")


# End