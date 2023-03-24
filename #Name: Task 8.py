#Name:                  Task 8.py
#Author:                Derek Baker
#Date Created:          23-03-2023
#Date Last Modified:    23-03-2023
#
#Purpose:
#
#The purpose of this program is to convert weight and length
#into the desired unit. The program will first ask if they want
#to convert speed or temperature, then ask if they want to convert
#from Kilograms to Pounds or vice versa, or if they want to 
#from Feet to Meters or vice versa.

def temperature(unit, number):
    global conversion 
    
    if unit == 'kg':
        conversion = number * 2.2
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' lbs')
        return True
    #converts the weight from Kilograms to Pounds and rounds it to the nearest 2 decimal places
    
    if unit == 'lb':
        conversion = number / 2.2
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' kg')
        return True
    #converts the temperature given from Pounds to Kilograms and rounds it to the nearest 2 decimal places
        
def speed(unit, number):
    if unit == 'm':
        conversion = number * 3.281
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' ft')
        return
    #converts from Meters to Feet and rounds to the nearest 2 decimal places
    
    if unit == 'ft':
        conversion = number * 0.304
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' m')
        return
    #converts from feet to meters and rounds to the nearest 2 decimal places

while True:
    try:
        decision = float(input("Would you like to convert weight or length: \n Weight [1] \n Length [2] \n"))
        if decision in range(1, 3):
            break
    except ValueError:
        print('Please enter a valid value: ')
    #program will only let the user input 1 or 2

#program starts here with asking the user if they want to convert a temperature or a speed

if decision == 1:
    unit = input("What is the unit you are converting from? 'KG' for Kilograms or 'LB' for Pounds:  ").strip().lower()
    while  not(unit == 'kg' or unit == 'lb'):
        unit = input('Please enter a valid value: ')
    while True:
        try:
            number = float(input("What is the Weight?: "))
            while number <= 0:
                number = float(input('Number cannot be zero. Please enter a valid value: '))
            temperature(unit, number)
            break
        except ValueError:
            print('Invalid entry. Try again: ')
        #program will catch any errors and have the user input a proper value
    
    
#if the user chooses to convert a temperature, the program will ask for which unit they are converting, and what the temperature is
#it will then call the function to do the conversion and then print it for the user

if decision == 2:
    unit = input("What is the unit you are converting from? 'M' for Meters, or 'FT' for Feet: ").strip().lower()
    while not(unit == 'm' or unit == 'ft'): 
        unit = input('Please enter a valid entry: ')
    while True:
        try: 
            number = float(input("What is the length?: "))
            while number <= 0:
                number = float(input('Number cannot be zero. Please enter a valid value: '))
            speed(unit, number)
            break
        except ValueError:
            print('Please enter a valid value: ')
        #program will loop until user enters a valid value. It will also not let the user enter in a value of 0 or lower
    
#if the user chooses to convert a speed, the program will ask for which unit they are converting and what the speed is. 
#it will then call the function to do the conversion and then print it for the user