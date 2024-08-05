# arithmetic operators
# addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# floor operator 
# => Returns an integer ignoring the remainder
print (20//3)
# Module (%) returns the remainder after division
print (20 % 3)

# Power(**)
print(20**5)
print("Power",20**2)

# Assignment operators
# =
a = 10
a+=20
a-=1
a=20
a%=3
print(a)

# Comparison operators
# variables
# Greater than (>)
# less than (<)
# equality (==)
# Greater than or equal to (>=)
# less than or equal to (<=)
# inequality to (!=)

print(20 >= 11)


# logical operators
# Logical AND (and)
print(20>16 and 11 == 11 and 11!= 11)
# if one of the statements is false then the whole statement is false
# Logical OR (or)
# if one of the conditions is true then the whole statement is true 
print (100 == 1 or 1 >2 or 39!=49)

# Conditional statements
x = 11
if x>20 :
    print("x is greater")
else :
    print(x ,"is lesser") 

number = int(input("Enter a number"))  
 
if number % 2 == 0 :
    print(number, "is even")
else :
    print(number,"is odd") 
        
