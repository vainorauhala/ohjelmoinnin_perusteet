print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    cel = float(input("Insert the amount of Celsius: "))
    fah = cel * 1.8 + 32
    print(f"{cel:.1f} °C equals to {fah:.1f} °F")

elif choice == 2:
    fah = float(input("Insert the amount of Fahrenheit: "))
    cel = (fah - 32) / 1.8
    print(f"{fah:.1f} °F equals to {cel:.1f} °C")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")