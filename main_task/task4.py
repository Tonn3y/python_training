# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email = input("Enter email:")
if (email.count("@") and len("@") == 1 ) and (email.count(".") and len(".") == 1):
    print("Valid email")
else:
    print("Invalid email")    

