# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

# phonenumber = input("Enter your contact:")

# if (phonenumber.startswith("07") and len(phonenumber) ==10 and phonenumber.isdigit()) or (phonenumber.startswith("+254") and len(phonenumber) == 13 and phonenumber.isdigit()) or (phonenumber.startswith("7") and len(phonenumber) == 9 and phonenumber.isdigit()) or (phonenumber.startswith("254") and len(phonenumber) == 12 and phonenumber.isdigit()) or (phonenumber.startswith("01") and len(phonenumber) == 10 and phonenumber.isdigit()) or (phonenumber.startswith("1") and len(phonenumber) == 9 and phonenumber.isdigit()) :
#     if phonenumber.startswith("07") or phonenumber.startswith("01"):
#         phonenumber = "+254" + phonenumber[1:]
#     elif phonenumber.startswith("7") or phonenumber.startswith("1"):
#         phonenumber = "+254" + phonenumber[0:] 
#     elif phonenumber.startswith("254") :
#         phonenumber = "+254" + phonenumber[3:]       

#     print(phonenumber) 

# else :
#     print("Incorrect format of input")

def contact () :
    phone_number = input("Enter a phone number: ")

    if phone_number[0:4] == "+254" and len(phone_number) == 13:
        phone_number = (f"{phone_number} is valid")
        print(phone_number)
    elif (phone_number[0:2] == "07" or phone_number[0:2] == "01") and len(phone_number) == 10:
        phone_number = "+254" + phone_number[1:]
        phone_number = (f"{phone_number} is valid")
        print(phone_number)
    elif (phone_number[0:1] == "7" or phone_number[0:1] == "1") and len(phone_number)==9:
        phone_number = "+254" + phone_number[0:]
        phone_number = (f"{phone_number} is valid")
        print(phone_number)
    elif phone_number[0:3]=="254" and len(phone_number)==12:
        phone_number = "+254" + phone_number[3:]   
        phone_number = (f"{phone_number} is valid")
        print(phone_number) 
    else :
        print("Invalid")

contact()        
