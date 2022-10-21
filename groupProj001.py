# ----------------------------------------------------------------------------------------------------------------------
# Author: Louis Silverstein
# Email: Louis@baraqu.com
# Date: 2022/10/20
# ----------------------------------------------------------------------------------------------------------------------
# Project: groupProj001
# Title: Basic Database Read/Write/View
# ----------------------------------------------------------------------------------------------------------------------
# Language: python
# Version: 3.7
# ----------------------------------------------------------------------------------------------------------------------
# Overview: Write a python program with two modules, 1) a data collection module to: collect user data and store the information in a text file on your system, and 2) a viewer module that lets the user view the data in the text file based on different parameters.
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Libs
# ----------------------------------------------------------------------------------------------------------------------
import json

# ----------------------------------------------------------------------------------------------------------------------
# Function Definitions
# ----------------------------------------------------------------------------------------------------------------------

def main():
    pass
    # run loadFileFunction()
    # prompt user for module ie (print, 1) is Input Data, 2) is View Data, 3) is Quit)
    # if 1
        # run inputModule(databaseObject)
    # if 2
        # run viewerModule(databaseObject)
    # if 3
        # run Quit()
    # else
        # Print (“You selected an invalid option, please try again!”)
        # rerun the option screen

def loadFileFunction():
    file = open('database.txt', encoding="utf8") # loads data from database.txt and put the object into 'file'

    data = file.read() # reads the infromation in the 'file' into python in a usable string format

    file.close()

    jsonData = json.loads(data)

    return jsonData

'''
############################################################################
database.txt - this file is going to live in the project folder and this is a sample bit of data
############################################################################
[{“firstName”: “John”, “lastName”: “Doe”, “alias”: “1337
haxzor”, “dob”: “03 / 23 / 74”, “email”: “1337 @ aol.com”, “timestamp”: “1594819641.9622827”}]
############################################################################
'''

def inputModule(databaseObject):
    pass
    # get data from user
    # variables to get (first name, last name, alias, dob, email, and timestamp)
    # input method and ask for input
    # save input into variable
    # review the data
    # if correct
        # save the input into the database
        # print do you want to add more data?
        # if yes
            # rerun the function
        # else
            # return the tempDatabase to the main program
    # else (if incorrect)
        # rerun the function to allow for different data to be input (go back to start)

def viewerModule(databaseObject):
    pass
    # ask the user how they want to view the data?
    # give 6 options (1) By First Name A-Z, 2) By Last Name A-Z 3)By Alias A-Z 4) By DOB 0+ 5) By Email A-Z 6) By Data Create 0+)
    # if input is 1, 2, 3, or 5
        # sort(databaseObject, Method) a-z by key {what is the method, that is the selection from the options above}
        # Print out the sorted data
        # Print do you want to view more data? If Yes, enter 1, if No enter 2.
        # if 1
            # Rerun the function
        # else (or if 2)
            # exit the function
    # if input is 4 or 6 (ie else)
        # Sort data numerically by key
        # Print out the sorted data
        # Print do you want to view more data? If Yes, enter 1, if No enter 2.
            # if 1
                # Rerun the function
            # else (or if 2)
                # exit the function

def sort(databaseObject, method):
    pass
    # methods are: firstName, lastName, alias, dob, email, timestamp

def quitProject(databaseObject):
    pass
    # save the file using the saveFileFunction(databaseObject)
    # tell the user that everything saved!
    # exit

def saveFileFunction(databaseObject):
    pass
    # take the database and write it to a file on the system
    # return success?

# ----------------------------------------------------------------------------------------------------------------------
# Main body
# ----------------------------------------------------------------------------------------------------------------------

