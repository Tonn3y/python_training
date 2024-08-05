marks = int (input("What's your marks?"))

if marks >= 70 :
    print("A")
elif marks >= 60 :
    print("B")
elif marks>= 50:
    print("C")
elif marks >= 40 :
    print("D")
elif marks >= 0 :
    print("Fail")
else :
    print("Error")


a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))

if a>b and a>c :
    print("a is the largest number")
elif b>c and b>a :
    print("b is the largest") 
elif b == a and a == c and b == c :
    print("They are equal") 
else :
    print("c is greater")   

