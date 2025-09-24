#Make a Python program, which prompts for a compound word.

#Get following aspects from the word
#Length
#First character
#Reversed version e.g. “Suitcase” is reversed “esactiuS”
#Display the aspects using print commands.
#Prompt the user to take substring from the existing compound word.
#Finally print the user specified substring.
#Program starting.
print("Program starting")

#Insert a closed compound word: Moonbanana
Word1 = input("Insert a closed compound word: ")
#The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
print(f"The word you inserted is '{Word1}' and in reverse it is {Word1[::-1]}.")
#The inserted word length is 10
print(f"The inserted word length is {len(Word1)}")
#Last character is 'a'
print(f"Last character is '{Word1[-1]}")

#Take substring from the inserted word by inserting...
print("Take substring from the inserted word by inserting...")
#1) Starting point: 0
word1start = int(input("1) Starting point: "))
#2) Ending point: 4
word1end = int(input("2) Ending point: "))
#3) Step size: 1
word1step = int(input("3) Step size: "))

Substring = Word1[word1start:word1end:word1step]
#The word 'Moonbanana' sliced to the defined substring is 'Moon'.
print(f"The word '{Word1}' sliced to the defined substring is '{Substring}'.")
#Program ending.#
print("Program ending.")