number = int(input("Enter a number to check if it's prime or not: "))

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
        print(f"{number} is a prime number")
