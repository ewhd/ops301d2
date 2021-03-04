#!/bin/bash

# Script:                       challenge303-file-permissions.sh
# Author:                       Ethan Denny
# Date of latest revision:      3/3/2021
# Purpose:     
#       Prompts user for input directory path.
#       Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#       Navigates to the directory input by the user and changes all files inside it 
#       to the input setting.
#       Prints to the screen the directory contents and the new permissions settings 
#       of everything in the directory.


# Define Variables
dir_path_var=""
permission_codes_var=""

# Define Functions


# Main

# This part prompts the user to input a directory path, stores it in dir_path_var, then displays a message 
# and the current permissions of every file in that directory
read -p "What is the path of the directory in which you would like to change permissions? " dir_path_var
echo "This program will change the permissions within $dir_path_var"
echo "The current permissions are:"
ls -al $dir_path_var

# This part gives information and then prompts the user for permission numbers and saves it as permission_codes_var
read -p "

| Representation | Decimal |
| - - -          |       0 |
| - - x          |       1 |
| - w -          |       2 |
| - w x          |       3 |
| r - -          |       4 |
| r - x          |       5 |
| r w -          |       6 |
| r w x          |       7 |

Please provide 3 decimal numbers from 0-7, corresponding with 
the read/write/execute permissions listed above, to change the 
permissions for Users, Group, and Others, respectively.

For example: 777 will give full permissions to all.
             000 will deny all permissions to all.

The permissions of every file in $dir_path_var will be changed.

What would you like to change permissions to? " permission_codes_var


# This part changes the permissions of every file in dir_path_var to the code values of permission_codes_var
chmod --recursive $permission_codes_var $dir_path_var


echo "The new permissions are"
ls -al $dir_path_var

#


# End