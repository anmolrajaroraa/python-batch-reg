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
originalEvenNumbers = [i for i in range(1,101) if ((i % 2 == 0)or(i % 3==0))]
evenNumbers = [i**2 for i in range(1,101) if ((i % 2 == 0) or (i % 3 == 0))]

newList = [(i**2 if ((i % 2 == 0) or (i % 3 == 0)) else 0) for i in range(1,101)]

#syntax 1 -> [expression, for loop, if condition]

print(originalEvenNumbers)
print(evenNumbers)
print(newList)

#membership operators - in, not in
#comparison operators - >,<,==,>=,<=,!=,not,is
#logical operators - and , or

print(4 in newList)
print(4 not in newList)
#print(10 > 20)
#print(10 < 20)
#print(10 == 20)
#print(10 >= 20)
print(10 <= 20)
print(10!=20)

list1 = [1,2,3]
list2 = [1,2,3,[1,2,3]]
list3 = [1,2,3]
list4 = list1
print(list1 in list2)
print(list1 == list3)
print(list1 is list3)
print(hex(id(list1)))
print(hex(id(list3)))
print(hex(id(list4)))
print(list1 is list4)

flag = False
if not flag:
    print("flag is true")