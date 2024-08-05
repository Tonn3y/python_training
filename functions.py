# def hello () :
#     name = "Tony"
#     print(f" Hello {name}")

# def rectanglearea () :
#     length = float(input("Enter length:"))
#     width = float(input("Enter width:"))
#     area = length * width
#     print(area)

# rectanglearea()

def evennumber () :
    number = float(input("Enter number:"))
    if number % 2 == 0:
        print(f"{number} is Even number")
    else :
        print(f"{number} is Odd number")   

evennumber()      
# 3,8,12,13   

def largest () :
    a = input("Enter number:")
    b = input("Enter number")
    c = input("Enter number")
    d = input("Enter number")

    if a>b and a>c and a>d :
        print(f"{a} is the largect")
    elif b>c and b>d and b>a :
        print(f"{b} is tge largest")
    elif c>a and c>b and c>d :
        print(f"{c} is the largest")
    else :
        print(f"{d} is the largest") 

largest()