#Make a Python program, which prompts user for a car brand and model. 
# After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters.

#Example program run:

#Program starting.
print("Program starting")
#Insert car brand: Toyota
Car_brand = input("Inser car brand: ")
#Insert car model: Corolla
Car_model = input("Insert car model: ")
#Car brand is "Toyota" and the model is 'Corolla'
print(f"Car brand is \"{Car_brand}\" ", end="")
print(f"and the model is '{Car_model}'.")
#Program ending.
print("Program ending.")