for num in range(1, 200+1, 1):
    if (num % 5) == 0 and (num % 3) == 0:
        print("fizz?buzz?")
    elif (num % 3) == 0:
        print("fizz")
    elif (num % 5) == 0:
        print("buzz")
    else:
        print(num)
