#Name:                  Task 8.py
#Author:                Derek Baker
#Date Created:          23-03-2023
#Date Last Modified:    23-03-2023
#
#Purpose:
#
#The purpose of this program is to convert temperature and speed
#into the desired unit. The program will first ask if they want
#to convert speed or temperature, then ask if they want to convert
#from Celcius to Fahrenheit or vice versa, or if they want to 
#from KPH to MPH or vice versa.

def temperature(unit, number):
    global conversion 
    if unit == 'c':
        conversion = (number * 1.8) + 32
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' F')
        return True
    #converts the temperature from Celcius to Fahrenheit and rounds it to the nearest 2 decimal places
    
    if unit == 'f':
        conversion = (number - 32) * 0.5556
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' C')
        return True
    #converts the temperature given from Fahrenheit to Celcius and rounds it to the nearest 2 decimal places
        
def speed(unit, number):
    if unit == 'kph':
        conversion = number / 1.609344
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' MPH')
        return
    #converts from KPH to MPH and rounds to the nearest 2 decimal places
    
    if unit == 'mph':
        conversion = number * 1.60934
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' KPH')
        return
    #converts from MPH to KPH and rounds to the nearest 2 decimal places

while True:
    try:
        decision = float(input("Would you like to convert temperature or speed: \n Temperature [1] \n Speed [2] \n"))
        if decision in range(3):
            break
    except ValueError:
        pass
    print('Please enter a valid value: ')

#program starts here with asking the user if they want to convert a temperature or a speed

if decision == 1:
    unit = input("What is the unit you are converting from? 'C' for Celcius or 'F' for Fahrenheit:  ").strip().lower()
    while  not(unit == 'c' or unit == 'f'):
        unit = input('Please enter a valid value: ')
    while True:
        try:
            number = int(input("What is the temperature?: "))
            temperature(unit, number)
            break
        except ValueError:
            pass
        print('Invalid entry. Try again: ')
    
    
#if the user chooses to convert a temperature, the program will ask for which unit they are converting, and what the temperature is
#it will then call the function to do the conversion and then print it for the user

if decision == 2:
    unit = input("What is the unit you are converting from? 'KPH' for Kilometers Per Hour to Miles Per Hour, or 'MPH' for Miles Per Hour to Kilometers Per Hour: ").strip().lower()
    while not(unit == 'kph' or unit == 'mph'): 
        unit = input('Please enter a valid entry: ')
    number = float(input("What is the speed?: "))
    speed(unit, number)
    
#if the user chooses to convert a speed, the program will ask for which unit they are converting and what the speed is. 
#it will then call the function to do the conversion and then print it for the user