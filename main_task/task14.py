# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True :
   a = input("Enter number:")
   b = input("Enter number:")

   if a.isdigit() and b.isdigit() :
       a = int(a)
       b = int(b)
       total = a + b
       break
   elif "." in a and "." in b :
       a = float(a)
       b = float(b)
       total = a + b
       break
   else :
       print("Invalid character entered")    

print(total)    

