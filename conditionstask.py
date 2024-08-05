# temperature = int(input("Enter the temperature:"))
# if temperature > 30 :
#     print("The temperature is troo high")
# elif temperature > 15 :
#     print("Normal temperature") 
# else :
#     print("Cold temperature")

# #Task2
# x = int(input("Enter number:"))
# y = int(input("Enter number"))

# if x >= 10 and x <=20 and y>100 :
#     print("Conditions met")
# else :
#     print("Conditions not met")

# #TAsk 3
# password = input("ENter password:")

# if password == "secret123" :
#     print("Access granted")
# else:
#     print("Access denied")

# student_score = int(input("Enter the student's score:"))
# attendance = int(input("Enter the attendance:"))  

# if student_score>90:
#     if attendance > 80:
#       print("Excellent student") 
#     else :
#         print("Good score,but attendance needs improvement") 
# else :
#     print("Improve on your score")           

# # Task 4

# num = int(input("Enter number"))

# if num>0 :
#     if num %2 ==0 and num %3 == 0:
#         print(f"{num} is positive and divisible by both 2 and 3")
#     elif num %2 == 0 :
#         print(f"{num} is divisible by two only")
#     elif num %3 == 0 :
#         print(f"{num} is divisible by three only") 
#     else :
#         print(f"{num} is neither divivsible by two nor three")          
# else :
#     print("Number is negative")   

# #Task 5
# username = input("Enter username")
# password = input("Enter passsword") 

# if username == "Ton3y" and password == "secret1234":
#     print("Login successful")
# else :
#     print("Login failed")   

# # Task 6
# x = input("Enter word:")
# if x[::-1] == x:
#     print(f"{x} is a palindrome")
# else :
#     print(f"{x} is not a palindrome") 

# Question4: Write a Python program that calculates the Body Mass Index (BMI) and categorizes it into Underweight, Normal weight, Overweight, and Obesity based on standard BMI ranges.
# Question5: Write a Python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# NB research on python loops
#Task 7
# weight = float(input("Enter weight:"))
# height = float(input("Enter height:"))
# bmi = weight/(height*height)
# if bmi<18.5 :
#     print("Underweight")
# elif bmi>=18.5 and bmi<=24.9 :
#     print("Normal weight")
# elif bmi>=25.0 and bmi<=29.9 :
#     print("Overweight")
# else :
#     print("Obesity")     

#Task 8
liss = []
x = list(range(1,101))
for num in x:
    if num% 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
        liss.append("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
        liss.append("Buzz")
    elif num % 3 == 0:
        print("Fizz") 
        liss.append("Fizz")
    else :
        liss.append(num)    

print(liss)           
                
  