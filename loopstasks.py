# Write a program that displays a numbers 1 to 50 inside a list.
x =  []
numbers = list(range(1,51))
for num in numbers :
    x.append(num)
print(x)    
# From 1 above display the ones divisible by 7 or 5 inside a list.
x = []
divisibleby7 = list(range(1,51))
for num in divisibleby7 :
    if num % 7 == 0 or num % 5 ==0:
       x.append(num)
print(x)    
# Find sum and average of values in the range between 10 to 40.
numbers = list(range(10,40))
total = 0
for num in numbers:
    total += num
average = total/len(numbers)

print(f"The total is: {total}")
print(f"The average is: {average}")
# Put in a list the first 10 odd numbers between 10 to 50.  
odd_numbers =[]
numcount = 0
numbers = list(range(10,50))
for num in numbers :
    if num != 0:
        odd_numbers.append(num)
        numcount +=1 
        if numcount == 10:
            break
print(odd_numbers)            

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number = int(input("Enter a number:"))
for num in range(1,11):
    print(f"{number} x {num} = {number * num}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
evencount = 0
evennumbers = list(range(1,50))
for even in evennumbers :
    if even %2 == 0:
        evencount += 1
print(f"The total number is:{evencount}")  

totalquantity = 0
ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
# Display the total quantity of the 3 above.
for i in ls1:
    quantity = i[1]
    totalquantity += quantity
print(totalquantity)

