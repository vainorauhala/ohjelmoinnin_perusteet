#Extend the previous menu program by adding three more options to the menu.

#Options:

#Print the name backwards
#Your name backwards is "{NameBackwards}"
#Print the first character
#The first character in name "{Name}" is "{FirstChar}"
#Show the amount of characters in the name
#There are {NameLength} characters in the name "{Name}"
#run 1 run 2 run 3 run 4 run 5 run 6
#Program starting.
print("Program starting.")
##This is a program with simple menu, where you can choose which operation the program performs the menu, please insert your name: John
name1 = input("This is a program with simple menu, where you can choose which operation the program performs the menu, please insert your name: ")


#Options:
print("Options:")
#1 - Print welcome message
print("1 - Print welcome message")
#2 - Print the name backwards
print("2 - Print the name backwards")
#3 - Print the first character
print("3 - Print the first character")
#4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
#0 - Exit
print("0 - Exit")
#Your choice: 1
choise = int(input("your choise: "))
#welcome John!
if(choise == 1):
    print(f"Welcome {name1}")
elif(choise == 2):
    print(f"Your name backward is {name1[::-1]}")
elif(choise == 3):
    print(f"The first character in name {name1} is {name1[:1]}")
elif(choise == 4):
    print(f"There are {len(name1)} characters in the name {name1}")
elif(choise == 0):
    print(f"Exiting...")
else:
    print(f"unknown opiton")
#Program ending.
print("\nProgram ending.")