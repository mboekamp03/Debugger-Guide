# Program Description
# The airline schedule program involves taking in data from the file flights.csv and then sorting this data into lists.
# From there, the user will have a list options to choose to output their desired information.
# After the user enters input, the program will execute the correct option and output information in either the terminal or in a new file.
# --------------------

# Algorithm Description
# -------------------
# 1. Sorting
# The selection sort algorithm takes the largest element and puts it in front of the list and then it works backwards
# This creates a sorted part of the list towards the beginning and unsorted towards the end
# This algorithm has a runtime of O(n^2)
# --------------------

# Program
# --------------------
# Function to open the file
# If a file with the name entered is in the folder the code is located in, it will open
# If one is not found, it will print invalid file name and ask user to try again
# Returns the opened file to the get data function
def openFile():
    goodFile = False
    while goodFile == False:
        # fname = input("Please enter a file name: ")
        fname = "example/flights.csv"
        try:
            flights = open(fname,'r')
            goodFile = True
        except IOError:
            print("Invalid filename try again ...")

    return flights

# Function to use an open file and add the data within it to lists
# Goes through each line in a file and adds the respective data to an empty list
# Splits each line at the commas and assigns each number seperated to a variable
# Returns the filled lists
def getData():
    flights = openFile()

    airlineList = []
    flightNumList = []
    departureList = []
    arriveList = []
    priceList = []

    # Goes through each line of code
    # Strips off any extra characters
    # Splits the line at the commas and adds each piece to its respective variable
    # Adds the variables to the lists
    # Closes the file
    for line in flights:
        line = line.strip()
        airline, num, depart, arrive, price = line.split(',')
        airlineList.append(airline)
        flightNumList.append(int(num))
        departureList.append(depart)
        arriveList.append(arrive)
        priceList.append(price)
    flights.close()

    return airlineList, flightNumList, departureList, arriveList, priceList

# Function to return the numerical value of a time entered
# Splits the time in the format of hour:minute into 2 functions for hours and minutes
# The string is split at the colon (:)
# Converts the variables to integers
# Then multiplies the hours by 60 to determine the correct time
# Adds the new hours value to the minutes which doesnt need to be adjusted
# Returns new time with those added
# Used whenever time is being compared
def duration (time):
    timeString = time

    hours, minutes = timeString.split(":")

    hours = int(hours) * 60
    minutes = int(minutes) 

    duration =  hours + minutes

    return duration

# Function to remove the $ from prices 
# Used throughout program to compare prices
# Changes price from $100.00 to 100.00
# Returns the adjusted price value
def finalPrice (price):
    price = (price.split("$")[1])
    price = float(price)
    price = "{:.2f}".format(price)
    return price 

# Reverts the price to 100 from 100.00
# Used to make the output correct
# Used only in the main function in the print statements
def revertPrice (price):
    price = float(price)
    price = "{:.0f}".format(price)
    return price

# Sorts the list by departure time
# Used in the function to write a new sorted file
# Dual selection sort algorithm
# Compares the numerical values of departure times and swaps the values
# Uses the duration function to calculate the numerical values of times
# Uses a copy of the list and swaps this list so the order of the original list is not changed
# Swaps the list of indexes
# Returns the sorted Lists
def sortLists(departureList):
    indexList = []
    newDepartList = departureList.copy()

    for i in range(len(departureList)):
        indexList.append(int(i))

    for i in range(0, len(newDepartList)):
        min = i
        for j in range(i + 1, len(departureList)):
            # comparison
            if duration(newDepartList[j]) < duration(newDepartList[min]):
                min = j + 1
        # swap
        indexList[i], indexList[min] = indexList[min], indexList[i]
        newDepartList[i], newDepartList[min] = newDepartList[min], newDepartList[i]

    return indexList
    # return list of indexs

# Called when the user enters 1 when asked for a choice
# Takes in the parameters of the lists
def findFlight(airlineList, flightNumList, departureList, arriveList, priceList):

    # First determines if an entered airline name is valid
    # To do this, it gets the input, then cycles through the airline name list and if a name is found, it moves on
    # Otherwise, it prompts the user for another input
    # This loop runs until a airline is found
    foundAirline = False 
    while foundAirline == False:
        airline = input("Enter airline name: ")
        for i in range (len(airlineList)):
            if airline == airlineList[i]:
                airlineTitle = airlineList[i]
                foundAirline = True
        if foundAirline == False:
            print("Invalid input -- try again")

    # If the airline is found, then this lists starts, it runs only while foundAirline is true
    # Uses the same process as the list above
    # Runs until a flight number is found
    # If found, sets the index of the found flight to airlineIndex
    foundNum = False
    if foundAirline == True:
        while foundNum == False:
            flightNumber = input("Enter flight number: ")
            for i in range (len(flightNumList)):
                if flightNumber == str(flightNumList[i]) and airlineTitle == airlineList[i]:
                    foundNum = True
                    airlineIndex = i
            if foundNum == False:
                print("Invalid input -- try again")

    # Uses these variables to return data from a specific flight
    # Returns these values
    airline = airlineList[airlineIndex]
    number = flightNumList[airlineIndex]
    depart = departureList[airlineIndex]
    arrive = arriveList[airlineIndex]
    price = priceList[airlineIndex]

    return airline, number, depart, arrive, price


# Function called when the user enters 2
# Takes in the lists as parameters
def maxDuration(airlineList, flightNumList, departureList, arriveList, priceList):

    # Determines if the number entered is valid
    # Uses a while loop to run until a valid number is found
    # Determines if the input is a number using the .isnumeric() function
    # If this is true, breaks out of the function
    # Gets the input in a string to avoid erros
    validNum = False
    while validNum == False:
        max = input ("Enter maximum duration (in minutes): ")
        if max.isnumeric() == True:
            validNum = True
        else:
            print("Entry must be a number")
    
    # Converts string to a integer after is is determines to be a number
    max = int(max)

    # Empty lists to store the new values because the function returns a list
    shortAirlineList = [] 
    shortFlightNumberList = []
    shortDepartList = []
    shortArriveList = []
    shortPriceList = []

    # Runs for the length of the lists and determines if the duration of the flight is less than or equal to the max
    # Computes this by calling the duration function
    # If the duration is less, it adds the orignal lists at index i to the new lists
    # Returns the new lists
    for i in range (len(arriveList)):
        length = int(duration(arriveList[i]) -  duration(departureList[i]))
        if (length <= max):
            shortAirlineList.append(airlineList[i])
            shortFlightNumberList.append(flightNumList[i])
            shortDepartList.append(departureList[i])
            shortArriveList.append(arriveList[i])
            shortPriceList.append(priceList[i])
    
    return shortAirlineList, shortFlightNumberList, shortDepartList, shortArriveList, shortPriceList

# Called when 3 is entered after user is prompted for a choice
# Function to determine the cheapest flight from a given airline
def cheapAirline(airlineList, priceList):
    # To take the user input and to determine it is valid
    # Runs until foundAirline is set to true
    # Checks to see if the name, which is input by the user, is equal to airlineList at index i
    # Once found, breaks out of the loop
    # If not found, user is prompted to try again
    foundAirline = False
    while foundAirline == False:
        name = input("Enter airline name: ")
        for i in range (len(airlineList)):
            if name == airlineList[i]:
                foundAirline = True
                break
        if foundAirline == False:
            print("Invalid input -- try again")

    # Creates a list to hold all instances of the single airline
    # Holds the index so I can access other lists at the same index
    singleAirline = []

    for i in range(len(airlineList)):
        if name == airlineList[i + 1]:
            singleAirline.append(i + 1)
    
    # Finds the cheapest index
    # Sets cheapest equal to the the priceList at the index of the first instance of the single airline
    # Cycles through each instance of the pricelist 
    # Only goes through the indexes which have the airline entered
    # As the list is cycled through, cheapest is adjusted and so is cheapest index
    # Returns the cheapest index
    cheapest = priceList[singleAirline[0]]
    cheapestIndex = singleAirline[0]
    for i in range(len(singleAirline)):
        if cheapest > priceList[singleAirline[i]]:
            cheapest = priceList[singleAirline[i]]
            cheapestIndex = singleAirline[i]

    return cheapestIndex

# Function to determine if the time entered in the lateFlight function is valid
# First determines if the entered time has a colon, if it does not, it is not a valid time so false is returned
# The determines if it has been split into 2 parts, if it has not, false is returned
# Checks to see if each part has a length of 2, if not false is returned
# Then, checks to see if the part is numeric
# If it is then it is checked to make sure the hours is between 1 and 23 and the minutes between 0 and 59
# If all these are true, the input is valid and true is returned
def validTime (time):
    if ':' in time:
        parts = time.split(":")
    else:
        return False

    if len(parts) != 2:
        return False
        
    if len(parts[0]) != 3 or len(parts[1]) != 3:
        return False

    if parts[0].isnumeric() == True and parts[1].isnumeric() == True:
        hours, minutes = int(parts[0]), int(parts[1])

        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            return False
            
    else:
        return False

    return True

# Called when 4 is entered as the user choice
# Function finds all flights after a time that is entered
def lateFlights(airlineList, flightNumList, departureList, arriveList, priceList):

    # The variable time is used to run the while loop as long as needed
    # Once a valid time is found, the loop ends
    # Counter is used to change the input request
    # The first time the user is asked for a time, the request is different
    # After the first time, the request begins with invalid time
    # Copies the flight time entered to a new variable because the function to determine the validity fo a time changes it
    # If the flight is not valid, the counter is incremented, changing the input request 
    # If it is found, time is set equal to true and the loop is ended
    time = False
    counter = 0
    while time == False:
        if counter == 0:
            flightTime = input("Enter earliest departure time: ")
        else:
            flightTime = input("Invalid time - Try again ")

        flightTimeCopy = flightTime

        if validTime(flightTime) == False:
            counter = counter

        else:
            time = True
            break

    # Empty loops to hold all flights after the input time
    lateAirlineList = [] 
    lateFlightNumberList = []
    lateDepartList = []
    lateArriveList = []
    latePriceList = []

    # Checks the numeric value of all the departure times and determines if they are greater (which is later) than the input
    # If it is greater, adds the list at index i to the new lists
    # Returns the new lists
    for i in range (len(departureList)):
        if duration(departureList[i]) > duration(flightTimeCopy):
            lateAirlineList.append(airlineList[i])
            lateFlightNumberList.append(flightNumList[i])
            lateDepartList.append(departureList[i])
            lateArriveList.append(arriveList[i])
            latePriceList.append(priceList[i])
    
    return lateAirlineList, lateFlightNumberList, lateDepartList, lateArriveList, latePriceList

# Function when the input for choice is 5
# Determines the average price by cycling through the price list
# Adds to the sum value which will hold the sum of all values
# Then divides by the length of the list
# Gets the correct format for average and returns it
def averagePrice (priceList):
    sum = 0
    for i in range (len(priceList)):
        current = finalPrice(priceList[i])
        sum = sum + float(current)

    average = sum / len(priceList)
    average = "{:.2f}".format(float(average))

    return average

# Called when the input for choices is 6
# First calls the sort lists function which is a dual sort alogorithm
# This function takes in the unsorted lists as parameters and returns the sorted lists
# Sets a variable called file name to time-sorted-flights.csv
# Opens the outfile with this name and a w to indcate I am writing to it
# Converts each value to a string and adds commas between them
# Close the file and return it
def sortFile (airlineList, flightNumList, departureList, arriveList, priceList):
    indexList = sortLists(departureList)

    fileName = "time-sorted-flights.csv"

    outFile = open(fileName, 'w')

    for i in range (len(airlineList)):
        outFile.write(str(airlineList[indexList[i]]) + "," + str(flightNumList[indexList[i]]) + "," + str(departureList[indexList[i]]) + "," + str(arriveList[indexList[i]]) + "," + str(priceList[indexList[i]]) + "\n")

    outFile.close()

    return fileName

# Menu for choices
# Calls validChoices and returns choice which it is set equal to
def getChoice():

    print("")
    print("Please choose one of the following options:")
    print("1 -- Find flight information by airline and flight number")
    print("2 -- Find flights shorter than a specified duration")
    print("3 -- Find the cheapest flight by a given airline")
    print("4 -- Find flight departing after a specified time")
    print("5 -- Find the average price of all flights")
    print("6 -- Write a file with flights sorted by departure time")
    print("7 -- Quit")

    choice = validChoice()

    return choice

# Function which is called in the get choice function 
# Uses a while loop to keep getting input if an invalid one is entered
# Determines if the choice is numeric
# Determines if the choice is between 1 and 7
# Returns choice
def validChoice():
    goodChoice = False
    while goodChoice == False:
        choice = input ("Choice ==> ")
        if choice.isnumeric() == True:
            if int(choice) > 0 and int(choice) < 9:
                goodChoice = True
                break
            else: 
                print("Entry must be between 1 and 7 ")
        else:
            print("Entry must be a number ")

    return int(choice)

# Calls getData to fill the lists
# Calls getChoice to get choice
# if the choice is not 7, the correct function is called and the correct values are printed
# After the correct values have been printed, getChoices is called again
# If 7 is the choice, the user exits the program
def main():
    airlineList, flightNumList, departureList, arriveList, priceList = getData()

    choice = getChoice()

    print("")

    while choice != 7:
        if choice == 1:
            airline, number, depart, arrive, price = findFlight(airlineList, flightNumList, departureList, arriveList, priceList)
            print("")
            print("The flight that meets your criteria is: ")
            print("")

            print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
            print(airline.ljust(8), str(number).ljust(6), depart.rjust(7),arrive.rjust(7),"$", revertPrice(finalPrice(price)).rjust(3))
            
            choice = getChoice()


        elif choice == 2:
            shortAirlineList, shortFlightNumberList, shortDepartList, shortArriveList, shortPriceList = maxDuration(airlineList, flightNumList, departureList, arriveList, priceList)
            print("")
            

            if len(shortAirlineList) > 0:
                print("The flights that meet your criteria are: ")
                print("")
                print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
                for i in range(len(shortAirlineList)):
                    print(shortAirlineList[i].ljust(8), str(shortFlightNumberList[i]).ljust(6), shortDepartList[i].rjust(7),shortArriveList[i].rjust(7),"$", revertPrice(finalPrice(shortPriceList[i])).rjust(3))
            else:
                print("No flights meet your criteria")
            
            choice = getChoice()
        

        elif choice == 3:
            cheapestIndex = cheapAirline(airlineList, priceList)
            print("")
            print("The flight that meets your criteria is: ")
            print("")

            print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
            print(airlineList[cheapestIndex].ljust(8), str(flightNumList[cheapestIndex]).ljust(6), departureList[cheapestIndex].rjust(7),arriveList[cheapestIndex].rjust(7),"$", revertPrice(finalPrice(priceList[cheapestIndex])).rjust(3))
            
            choice = getChoice()
        

        elif choice == 4:
            lateAirlineList, lateFlightNumberList, lateDepartList, lateArriveList, latePriceList = lateFlights(airlineList, flightNumList, departureList, arriveList, priceList)
            print("")

            
            if len(lateAirlineList) > 0:
                print("The flights that meet your criteria are: ")
                print("")
                print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
                for i in range(len(lateAirlineList)):
                    print(lateAirlineList[i].ljust(8), str(lateFlightNumberList[i]).ljust(6), lateDepartList[i].rjust(7),lateArriveList[i].rjust(7),"$", revertPrice(finalPrice(latePriceList[i])).rjust(3))
            else:
                print("No flights meet your criteria")
            
            choice = getChoice()


        elif choice == 5:
            average = averagePrice(priceList)
            average = "{:.2f}".format(float(average))

            print("The average price is $", average) 
            
            choice = getChoice()
            
        elif choice == 6:
            fileName = sortFile (airlineList, flightNumList, departureList, arriveList, priceList)
            
            print("Sorted data has been written to file: ", fileName)
            
            choice = getChoice()
    else:
        print("Thank you for flying with us")


main()