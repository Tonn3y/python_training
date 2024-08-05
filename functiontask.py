# def largest () :
#     a = input("Enter number:")
#     b = input("Enter number")
#     c = input("Enter number")
#     d = input("Enter number")

#     if a>b and a>c and a>d :
#         print(f"{a} is the largect")
#     elif b>c and b>d and b>a :
#         print(f"{b} is tge largest")
#     elif c>a and c>b and c>d :
#         print(f"{c} is the largest")
#     else :
#         print(f"{d} is the largest") 

# largest()

def speed () :
    speed = int(input("Enter speed:"))
    if speed < 70 :
      print("OK")      
    else:
      points = (speed - 70)/5
      points += 0.5
      points = round(points)
      if points < 12 :
          print(points)  
      else:
            print("License revoked")

speed()          


# def stocktotal() :
#     prods = [["omo","30kshs","300"], ["milk","50kshs","200"],["bread","45ksh","359"], ["coffee","5kshs","79"]]
#     totalstock = 0

#     for stock in prods :
#         totalstock += int(stock[2])

#     print(totalstock)

# stocktotal()

# def verification() :
#     correctemail = "admin@mail.com"
#     correctpassword = "Admin@123"
#     attempts = 4
#     for i in range(attempts) :
#         email = input("Enter email:")
#         password = input("Enter password:")
#         if password == correctpassword and email == correctemail :
#             print("Access granted")
#             break
#         else :
#             if i < attempts - 1 :
#                 print(f"Wrong attempt.You have {attempts - i -1} remaining")
#             else :
#                 print("You have been blocked")      

# verification()

def total (a,b,c,d,e) :
    total = a + b + c + d + e
    return total

math = int(input("Maths:"))
english = int(input("English:"))
kiswahili = int(input("Kiswahili:"))
science = int(input("Science:"))
socialstudies = int(input("Socialstudies:"))
total = total(math,english,kiswahili,science,socialstudies)

def average(sum) :
    average = sum/5
    return average
average = average(total)

def grades (a) :
    if a > 79 :
        return ("A")
    elif a >=60 :
        return ("B")
    elif a >= 49 :
        return ("C")        
    elif a >= 40 :
        return ("D")
    elif a >= 0 :
        return ("E")        
    else :
        return ("Error")    

grade = grades(average) 
print(grade)