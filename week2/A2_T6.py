#write a Phyton program which asks user to insert hex color.
#In this case hex color is expected to be the 7 character,
#representation starting with # and followed by 6 0-f,
#characters to represent RGB colors.
#slice the amount of red, green and blue from that inserted,
#color and display each color as shown below.

#Example program run:

#Program starting
print("Program starting.\n")
#Insert a hex color: #FFA500
Hexcolor = input("Insert a hex color: ")
#Colors
print("Colors")
#- Red FF
print(f"- Red {Hexcolor[1:3]}")
#- Green A5H}")
print(f"- Green {Hexcolor[3:5]}")
#- Blue 00
print(f"- Blue {Hexcolor[5:7]}\n")
#Program ending
print("Program ending")