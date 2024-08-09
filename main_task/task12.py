# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
a = input("Enter number:")
b = input("Enter number")
c = input("Enter number")
d = input("Enter number")

if a>b and a>c and a>d :
    print(f"{a} is the largect")
elif b>c and b>d and b>a :
    print(f"{b} is the largest")
elif c>a and c>b and c>d :
    print(f"{c} is the largest")
elif d>a and d>b and d>c :
    print(f"{d} is the largest") 
else :
    print(f"{a},{b},{c},{d} are all equal")               