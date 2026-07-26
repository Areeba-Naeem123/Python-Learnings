

clr = input("what is the clr of your banana ?")
clr = clr.lower()
ripness=""
if (clr=="yellow"):
    ripness="unrip"
elif(clr=="green"):
    ripness="rip"
elif(clr=="brown"):
    ripness="overrip"
else: 
    print ("not categorized")
    exit()

print(ripness)
