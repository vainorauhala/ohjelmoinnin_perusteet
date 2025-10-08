#Make Python program and implement if-statements 
# in proper places.

#Ask user to insert two integers
#Compare the integers and then announce the greater number
#Create sum of the two integers
#Check the parity of the sum (see modulo-operator ‘%’)
#Other possible output variants:

#Integer comparison
#Integers are the same.
#First integer is greater.
#Parity check
#Sum is even.
#Example program run

#run 1 run 2 run 3
#Program starting.
print("Program starting.")
#Insert two integers.
print("Insert two integer.")
#Insert first integer: 5
Int1 = input("Insert first integer: ")
Int1 = int(Int1)
#Insert second integer: 5
Int2 = input("Inser second integer:")
Int2 = int(Int2)
#Comparing inserted integers.
if(Int1 > Int2):
    Print("First integer is greater.")
elif(Int2 > Int2):
    print("Second integer is greater")
#Integers are the same
else:
    print("Integers are the same")
#Adding integers together
sum = Int1 + Int2
#5 + 5 = 10
print(f"{Int1} + {Int2} = {sum}")
#checking the parity of the sum...
Remainder = sum % 2
#Sum is even.
if(Remainder == 0):
    print("Sum is even")
else:
    print("sum is odd.")
#Program ending.
print("Program ending.")