#!/user/bin/env python3

# Script:                       challenge307-directory-creation.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/9/2021
# Purpose:     
#           This script generates all directories, sub-directories and files for a 
#           user-provided directory path.


# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
path_var = input("Enter path: ")


# Declaration of functions

### Declare a function here

def bash_walk(path):
    for (root, dirs, files) in os.walk(path):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here

bash_walk(path_var)

# End