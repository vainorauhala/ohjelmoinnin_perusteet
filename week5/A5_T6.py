
def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice()-> int:
    choice = int(input("Your choice: "))
    return int(choice)



def main():
    print("Program starting")
    showOptions()
    choice = -1
    choiceCount = 0
    while choice != 0:
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {choiceCount}")
        elif choice == 2:
            choiceCount += 1
            print("Count increased!")
        elif choice == 0:
            print("Exiting program.")
        elif choice == 3:
            choiceCount = 0
            print("Cleared count!")
        else:
            print("Unknown option!")
    print()
    print("Program ending.")

main()