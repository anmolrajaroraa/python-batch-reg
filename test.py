#num1 = 10
#num2 = 20
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
sub = str(num1 - num2)
mul = str(num1 * num2)
div = num1 / num2 #classic division
div2 = num1 // num2 #floor division

print(num1 + num2)

# - single line comment
''' multi
line comment
'''

#if we use comma in print statement we would get no error for types,
#and we get one space on both sides of our variable value
#if we use + for concatenation in print statement we would get errors,
#we can solve this error using type casting, and there is no spaces given automatically

#print("Sum of num1 and num2 is " + total)
#print("Sum of num1 and num2 is ", total)
print("Sum of",num1,"and",num2,"is",total)
#print("Sum of "+str(num1)+" and "+ str(num2)+" is "+str(total)) #type casting

#print("Difference between %d and %d is %s"%(num1,num2,sub))
print("Difference between {} and {} is {}".format(num1, num2, sub))

print("Product of {} and {} is {}".format(num1, num2, mul))

print(f"Division of {num1} by {num2} is {div2}")
