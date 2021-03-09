#!/user/bin/env python3

# Script:                       challenge306-bash-in-py.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/8/2021
# Purpose:     
#           Demonstrate the use of the python "os" library to wrap bash commands in python
#           Declare three python variables that contain bash commands
#           Call the python function print() three times


# Import libraries:
import os     #this imports "operating system dependent functinality"

# Use the syntax library.function(parameter) to call a command known to the OS
# In this case, we are using a linux system so we will call bash commands
# Thus, our commands will look like os.system(BASH_COMMAND)


# Define variables

# These three variables hold bash commands as strings
whoami_com = "whoami"
get_network_info_com = "ip a"
get_hardware_info_com = "lshw -short"


# Define Functions

# This function takes a string containing abash command as an argument and returns 
# an explanation string and then the output of the command
def bash_demo(command):
    print('Execute the bash command "' + command + '"')
    os.system(command)

# Main

# These lines call the bash functions stored in variables above
# Cosmetic lines have been inserted between to visually separate results
bash_demo(whoami_com)
print()
bash_demo(get_network_info_com)
print()
bash_demo(get_hardware_info_com)

# End