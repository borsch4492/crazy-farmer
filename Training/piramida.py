floursN = int(input("How many flours? "))
for flour in range(1, floursN+1, 1):
    #print(flour)
    bricks = " "*(floursN-flour)
    bricks = bricks +"#"*(flour*2-1)
    print(bricks)
print("done.")
