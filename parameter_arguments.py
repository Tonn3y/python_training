# # def hello (name) :
# #     print(f" Hello {name}")

# # # hello("Tony")
# # fname = input("Enter name:")
# # hello(fname)

# # # Create function for calculating area of a triangle

# # def area(base , height) :
# #     area = 0.5 * base * height
# #     return area

# # base = int(input("Enter base :"))
# # height = int(input("Enter height :"))
# # thearea = area(base,height)
# # print(thearea)

# # def arearerectangele(a,b) :
# #     area = a * b
# #     return area
# # length = int(input("Enter length:"))
# # width = int(input("Enter width:"))
# # rectangle = arearerectangele(length,width)
# # print(rectangle)

# def evenorodd (num) :
#     if num % 2 == 0 :
#         result = (f"{num} is even")
#     else :
#         result = (f"{num} is odd")
#     return result    

# number = int(input("Enter a number:"))
# num = evenorodd(number)
# print(num)      

# #  3 8 10 12 13

# def penalty (speed) :
#     if speed < 70 :
#       result = "OK"      
#     else:
#       points = (speed - 70)/5
#       points += 0.5
#       points = round(points)
#       if points < 12 :
#           result = points
#       else:
#             result = "License revoked" 
#     return result        

# speed = int(input("Enter speed:"))  
# print (penalty(speed))

# def contact (phone_number) :

#     if phone_number[0:4] == "+254" and len(phone_number) == 13:
#         phone_number = (f"{phone_number} is valid")
#         result = phone_number
#     elif (phone_number[0:2] == "07" or phone_number[0:2] == "01") and len(phone_number) == 10:
#         phone_number = "+254" + phone_number[1:]
#         phone_number = (f"{phone_number} is valid")
#         result = phone_number
#     elif (phone_number[0:1] == "7" or phone_number[0:1] == "1") and len(phone_number)==9:
#         phone_number = "+254" + phone_number[0:]
#         phone_number = (f"{phone_number} is valid")
#         result = phone_number
#     elif phone_number[0:3]=="254" and len(phone_number)==12:
#         phone_number = "+254" + phone_number[3:]   
#         phone_number = (f"{phone_number} is valid")
#         result = phone_number 
#     else :
#         result = "Invalid"
#     return result    

# phone_number = input("Enter a phone number: ")
# phone_number = contact(phone_number)
# print(phone_number)

def totalstockincompany (a) :
    totalstock = 0

    for stock in a :
        totalstock += int(stock[2])

    return totalstock

prods = [["omo","30kshs","300"], ["milk","50kshs","200"],["bread","45ksh","359"], ["coffee","5kshs","79"]]

totalstockincompany = totalstockincompany(prods)
print(totalstockincompany)

# def largestnumber (a,b,c,d) :

#     if a>b and a>c and a>d :
#         result = f"{a} is the largect"
#     elif b>c and b>d and b>a :
#         result = (f"{b} is the largest")
#     elif c>a and c>b and c>d :
#         result = (f"{c} is the largest")
#     else :
#         result = (f"{d} is the largest") 
#     return result     

# a = input("Enter number:")
# b = input("Enter number:")
# c = input("Enter number:")
# d = input("Enter number:")   

# largestnumber = largestnumber(a,b,c,d)
# print(largestnumber)

def verify () :
    correctemail = "admin@mail.com"
    correctpassword = "Admin@123"
    attempts = 3

    for i in range(attempts) :
        email = input("Enter email:")
        password = input("Enter password:")   
        if password == correctpassword and email == correctemail :
            result = ("Login successful")
            break
        else :
            if i < attempts -1 :
                print ("Invalid username or password")
            else :
                result = ("You have been blocked")   
    return result             

verification = verify ()
print(verification) 