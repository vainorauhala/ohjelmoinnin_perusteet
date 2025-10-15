
print("Program starting.")
print()
print("Check multiplicative persistence.")
numb = int(input("Insert an integer:"))

stepcount = 0

digits = [int(d) for d in str(numb)]

while len(str(numb)) > 1:
    digits = [int(d) for d in str(numb)]
    result = 1
    for d in digits:
        result *=d
    
    print(" * ".join(str(d) for d in digits), "=", result)

    stepcount +=1
    numb = result

print("No more steps.")
print()
print(f"This program took {stepcount} steps(s)")
print()
print("Program ending.")

