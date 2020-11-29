maxN = (2**82589933) -  1 #input("Enter the max number: ")
for num in range(1, maxN+1, 1):
    decounter = 0
    for devider in range(1, maxN+1, 1):
        if (num % devider) == 0:
            decounter += 1
            #print("etoprosroechislo")
    #########print(num)
    if decounter <= 2:
        print(num)##########print("EtoProsroeChislo") #wery weird
