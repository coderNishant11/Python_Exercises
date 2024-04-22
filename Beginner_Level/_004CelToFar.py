# Develop a program to convert Celsius to Fahrenheit.
print('Welcome to Celsius to Fahrenheit')
celsius= float(input('Enter celcious value: '))

def celToFahr(cel):
    fahr= (9*cel/5)+32
    return fahr

fahrenheitValue=celToFahr(celsius)

print('{} celsius is equal to {} fahrenheit'.format(celsius,fahrenheitValue))