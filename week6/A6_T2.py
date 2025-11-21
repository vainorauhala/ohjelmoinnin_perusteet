print("Program starting")
firstname = input("Insert first name: ")
lastname = input("Insert last name: ")
filename = input("Insert filename: ")


file = open("data.txt", "w")
file.write(firstname + '\n')
file.write(lastname + '\n')

file.close()
print("Program ending")