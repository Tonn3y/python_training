# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

correctpassword = "admin@123"
attempts = 4

for i in range(attempts) :
    password = input("Enter password:")
    if password == correctpassword :
        print("Access granted")
        break
    else :
        if i < attempts-1 :
            print(f"Incorrect password {attempts - i -1} attempts left") 
        else :
            print("Account blocked")   

password = input("Enter a password: ")

# attempts = 4
# password = input("Enter password:")
# while password != "admin@123":
#     attempts -= 1
#     if attempts == 0:
#         print("Account blocked")
#         break
#     password = input("Incorrect password. Try again: ")

# if password == "admin@123":
#     print("Access granted") 
# password = input("Enter password:")
# correctpassword = "admin@123"
# if password != correctpassword :
#     password = input("Enter password:")
#     if password != correctpassword :
#         password = input("Enter password:")
#         if password != correctpassword :
#             password = input("Enter password:")
#             if password != correctpassword :
#                 print("access denied")
            

# else :
#      print("access granted")
        