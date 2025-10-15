# tee  muuttuja joka laskee kierrokset
# muua annettu arvo integeriks
# arvomuuttuu loopin aikana.
# tee while- loop joka looppaa niin kauan kuin
# luku ei ole 1
#     prijttaa alkuperäinen arvo ja lisää ->
#     testaa onko arvo parillinen (jakojäännöslasku)
#         jaa arvo kahdella jos se on parillinen
#     tai muussa tapauksessa 
#         kerro arvo kolmella ja lisää 1

#     lisää kierroksiin +1
# printtaa kierrokset

print("Program starting.")

luku = int(input("Insert a positive integer: "))

stepcount = 0

print(luku, end="")  

while luku != 1:
    if luku % 2 == 0:
        luku = luku // 2          
    else:
        luku = 3 * luku + 1        
    print(f" -> {luku}", end="")   
    stepcount += 1                 

print(f"\nSequence had {stepcount} total steps.")
print()
print("Program ending.")
