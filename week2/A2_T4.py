#Prompt the user to insert the minutes spent on each previous topic task.
#Calculate the sum and the average. 
#Display those in the example program run format(Note! precision). 
#Make sure to calculate the required average for two decimal digits and 
#later integer as rounded integer (precision 0 + type conversion).


# Example program run:

#Program starting.
print("Program starting.")
#Estimate how many minutes you spent on programming...
print("Estimate how many minutes you spent on programming....\n")
A1T1 = int(input("A1_T1: "))
A1T2 = int(input("A1_T2: "))
A1T3 = int(input("A1_t3: "))
A1T4 = int(input("A1_T4: "))
A1T5 = int(input("A1_T5: "))
A1T6 = int(input("A1_T6: "))
A1T7 = int(input("A1_T7: "))

Total = A1T1 + A1T2 + A1T3 + A1T4 + A1T5 + A1T6 + A1T7
Average = float(Total / 7)
#A1_T1: 3
#A1_T2: 7
#A1_T3: 9
#A1_T4: 8
#A1_T5: 13
#A1_T6: 14
#A1_T7: 21

#In total you spent 75 minutes on programming.
print(f"\nIn total you spent {Total} minutes on programming.")
#Average per task was 10.71 min and same rounded to the nearest integer 11 min.
print(f"Average per task was {round(Average,2)} min and same rounded to the neares integer {round(Average)} min.")

#Program ending.
print("Program ending.")