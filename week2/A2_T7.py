#Create a Python program to convert Fahrenheit to Celcius. 
# Round the Celsius to 1 decimal precision.

#Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

#Example program run:

#Program starting.
print("Program starting.")
#Insert fahrenheits: 50
fahrenheit = float(input("Insert fahrenheits: "))
celsius = (fahrenheit - 32)/ 1.8
#50.0°F is 10.0°C
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C")
#Program ending.
print("Program ending.")