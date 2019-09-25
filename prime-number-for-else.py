'''number = int(input("Enter a number to check if it's prime or not: "))

numberIsPrime = True

if number <= 1:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number//2):
        if number % i == 0:
            numberIsPrime = False
            print(f"{number} is not a prime number")
            break

    if numberIsPrime:
        print(f"{number} is a prime number")'''




number = int(input("Enter a number to check if it's prime or not: "))

if number <= 1:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number//2):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")

#if for loop runs till end, else will also run
#but if we break for loop in between on some condition,
# else will also be deleted from memory and will not run
