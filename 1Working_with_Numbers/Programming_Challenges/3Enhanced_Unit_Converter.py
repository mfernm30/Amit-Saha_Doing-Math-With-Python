from fractions import Fraction

'''
Unit converter: Miles and Kilometers
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')
    print('5. Kilograms to Pounds')
    print('6. Pounds to Kilograms')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    lb = kg * 2.20462
    print('Weight in pounds: {0}'.format(lb))

def pounds_kg():
    lb = float(input('Enter weight in pounds: '))
    kg = lb / 2.20462
    print('Weight in pounds: {0}'.format(kg))

def celsius_Fahrenheit():
    c= float(input('Enter temperature in Celsius: '))
    f = (c*Fraction(9,5)) +32
    print('Temperature in Fahrenheit: {0}'.format(f))

def fahrenheit_Celsius():
    f= float(input('Enter temperature in Fahrenheit: '))
    c = (f-32) * Fraction(5,9)
    print('Temperature in Celsius: {0}'.format(c))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        celsius_Fahrenheit()
    if choice == '4':
        fahrenheit_Celsius()
    if choice == '5':
        kg_pounds()
    if choice == '6':
        pounds_kg()