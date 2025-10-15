print("Program starting.")
startpoint = int(input("Insert starting poins: "))
stoppoint = int(input("Insert stopping point: "))
inceptionpoin = int(input("Insert stoppig point: "))
("")
if (startpoint >= stoppoint):
    print("Starting point value must be less than the stopping point value." \
    "Inspection value must be within the range of start and stop.")
    Run = False
if ((startpoint > inceptionpoin) or (inceptionpoin > stoppoint)):
    print("Inspection value must be within the range of start and stop.")
    Run = False
("")
if(Run == True):
    print("First loop- inspection with break:")
    for i in range(startpoint, stoppoint):
        if(i == inceptionpoin):
            break
        else:
            if(i == (stoppoint-1)):
                print(i)
            else:
                print(i, end=' ')

    print("")
    print("Second loop - inspection with continue:")

print("Program ending.")