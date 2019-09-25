print('''
1.add
2.subtraction
3.multiply
4.division
''')
c=int(input("enter choice"))
a=int(input("enter first number"))
b=int(input("enter first number"))
if c==2:
    ans=a-b if a>b else b-a
    print("result",ans)
elif c==1:
    ans=a+b if a>=0 and b>=0 else print("Enter positive integer")
    print("result",ans)
elif c==3:
    ans=a*b
    print("result",ans)
else:
    ans=a/b
    print("result",ans)