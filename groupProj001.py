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
# # ----------------------------------------------------------------------------------------------------------------------
import json
import time

# ----------------------------------------------------------------------------------------------------------------------
# Function Definitions
# ----------------------------------------------------------------------------------------------------------------------

def main(databaseObject):
    print("Welcome to the Database Application!")

    running = True
    while running == True:

        print("Please make a selection:")
        print("1) Input new data into database")
        print("2) View data in database")
        print("3) Quit")

        selection = input("Selection:" )

        if selection == "1":
            inputModule(databaseObject)

        elif selection == "2":
            viewerModule(databaseObject)

        elif selection == "3":
            quitProject(databaseObject)

def loadFileFunction():
    file = open('database.txt', encoding="utf8") # loads data from database.txt and put the object into 'file'

    data = file.read() # reads the information in the 'file' into python in a usable string format

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
    runInput = True     #the first time our function runs it sets the loop to start by default
    tempDatabase = databaseObject  # take our database and make a copy so we can do something to it

    while runInput == True:

        # get data from user
        print("=======================")
        print("===== Input Module ====")
        print("=======================")

        print("Please follow the prompts for the desired input")
        # variables to get (first name, last name, alias, dob, email, and timestamp)
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        alias = input("Alias: ")
        dob = input("Date Of Birth (YYYY/MM/DD): ")
        email = input("Email Address: ")
        timestamp = time.time()

        # save input into variable

        tempDatabaseObject = {"firstName" : firstName, "lastName" : lastName, "alias" : alias, "dob" : dob, "email" : email, "timestamp" : timestamp}

        # review the data
        print("Please Review the following data:", tempDatabaseObject)

        response = input("Is the above data correct (Y or N):")

        if response.upper() == "Y":

            # save the input into the database
            tempDatabase.append(tempDatabaseObject)

            # print do you want to add more data?
            response = input("Do you want to add another entry? (Y or N):")

            if response.upper() == "Y":
                runInput = True

            else:
                runInput = False

        else:
            runInput = True

    return tempDatabase

def viewerModule(databaseObject):
    runInput = True  # the first time our function runs it sets the loop to start by default
    tempDatabase = databaseObject  # take our database and make a copy so we can do something to it

    while runInput == True:
        # ask the user how they want to view the data?
        # give 6 options (1) By First Name A-Z, 2) By Last Name A-Z 3)By Alias A-Z 4) By DOB 0+ 5) By Email A-Z 6) By Data Create 0+)
        print("=======================")
        print("===== Viewer Module ====")
        print("=======================")

        print("How would you like the view the data?")
        print("1) By Fist Name A-Z")
        print("2) By Last Name A-Z")
        print("3) By Alias A-Z")
        print("4) By DOB Ascending")
        print("5) By Email A-Z")
        print("6) By Date Created Ascending")

        selection = input("Selection: ")

        if selection == "1":
            databaseView = sorted(tempDatabase, key=lambda d: d['firstName'])
            linebyline(databaseView)

        elif selection == "2":
            databaseView = sorted(tempDatabase, key=lambda d: d['lastName'])
            linebyline(databaseView)

        elif selection == "3":
            databaseView = sorted(tempDatabase, key=lambda d: d['Alias'])
            linebyline(databaseView)

        elif selection == "4":
            databaseView = sorted(tempDatabase, key=lambda d: d['dob'])
            linebyline(databaseView)

        elif selection == "5":
            databaseView = sorted(tempDatabase, key=lambda d: d['email'])
            linebyline(databaseView)

        elif selection == "6":
            databaseView = sorted(tempDatabase, key=lambda d: d['timestamp'])
            linebyline(databaseView)

        else:
            print("You entered an invalid selection, please try again:")

        # print do you want to add more data?
        response = input("Do you want to view the data in a different way? (Y or N):")

        if response.upper() == "Y":
            runInput = True

        else:
            runInput = False

def quitProject(databaseObject):
    saveFileFunction(databaseObject)
    print("Congrats the database has been updated!")
    quit()

def saveFileFunction(databaseObject):
    # take the database and write it to a file on the system
    textDatabase = json.dumps(databaseObject)

    f = open("database.txt", "w")
    f.write(textDatabase)
    f.close()

    # return success?
    return True

def linebyline(input):
    for lines in input:
        print(lines)

# ----------------------------------------------------------------------------------------------------------------------
# Main body
# ----------------------------------------------------------------------------------------------------------------------

database = loadFileFunction()  # load the database file from the text object
main(database)


