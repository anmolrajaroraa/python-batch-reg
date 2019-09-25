a = 100
b = 20
c = a + b
# if a > b:
#     d = a-b
# else:
#     d = b-a

d = (a - b) if (a > b) else (b - a)

#d = a > b ? a - b : b - a

print(f"Sum of {a} and {b} is {c}")
print(f"Diff between {a} and {b} is {d}")

listOfEvenNumbers = []

# for i in range(1,101):
#     if i % 2 == 0:
#         listOfEvenNumbers.append(i)

# for i in range(1,101):
#     listOfEvenNumbers.append(i) if (i % 2 == 0) else False

# for i in range(2,101,2):
#     listOfEvenNumbers.append(i)

# for i in range(1,101):
#     if i % 2 == 0 and i % 3 == 0:
#         listOfEvenNumbers.append(i)

# for i in range(1,101):
#     if i % 2 == 0 or i % 3 == 0:
#         listOfEvenNumbers.append(i)

# for i in range(1,101):
#     listOfEvenNumbers.append(i) if ((i % 2 == 0) or (i % 3 == 0)) else False

#List Comprehension
evenNumbers = [i for i in range(1,101) if ((i % 2 == 0) or (i % 3 == 0))]

print(evenNumbers)