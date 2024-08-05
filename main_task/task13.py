# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

correctemail = "admin@mail.com"
correctpassword = "Admin@123"
attempts = 3

for i in range(attempts) :
    email = input("Enter email:")
    password = input("Enter password:")
    if password == correctpassword and email == correctemail :
        print("Login successful")
        break
    else :
        if i < attempts -1 :
            print("Invalid username")
        else :
            print("You have been blocked")    
