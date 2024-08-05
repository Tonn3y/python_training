# For loops
# Used to iterate through a sequence
# while loop
# used to execute a sequence as long as the condition is true
# Nested loops
# Loops exisiting inn other loops
# for i in range(0,10,2) :
#     print(i)

# x = list(range (900,1001)) 
# for num in x :
#     print(num)

# numbers = list(range(20,501))
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         continue

# pas = 3
# password = input("Enter password:")
# for i in password :
#     if password == "secret123" :
#         print("Access granted")
#         break
#     else :
#         print("Try again")    

even_numbers = []
numbers = list(range(0,201))
for num in numbers :
    if num %2 == 0:
        even_numbers.append(num)
        if num == 80:
            break
print(even_numbers)  

print("break")

odd_numbers = []
odd = list(range(20,101))
for i in odd :
    if i % 2 !=0 :
        odd_numbers.append(i)
print(odd_numbers)        
