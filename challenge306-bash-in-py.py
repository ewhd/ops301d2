#!/user/bin/env python3

# Script:                       challenge306-bash-in-py.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/8/2021
# Purpose:     
#           


# Import libraries:
import os     #this imports "operating system dependent functinality"

# Call the "system" function for the "os" library to run the command "ls"
# library.function(parameter) is the syntax

# Define variables
whoami_output = ""
network_info = ""
hardware_info = ""

# Define Functions

# This is a generalized function to operate a bash command within python3
# Requires the os libary be imported
def bash_func(command):
    os.system(command)


# Main

whoami_output = bash_func("whoami")
print(whoami_output)