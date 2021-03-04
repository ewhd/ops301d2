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