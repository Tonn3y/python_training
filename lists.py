# Creating lists
Students = ["Tom","Samuel","Diana","Tess","Keziah","Tony"]
print(type(Students))
# Months
Months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
print(Months[2])
# Modify numbers in a list
numbers = ["1","2","3","4"]
numbers[1] = "Josh"
print(numbers)
# slicing
print(numbers[0::3]) 
fruits = ["Grapes","Mango","Avocado","Tangerines"]
print(fruits[1::3])
#append
fruits.append("Apples")
print(fruits)
#pop
fruits.pop()
print(fruits)
# copy
x = fruits.copy()
print(x)
# count
print(fruits.count("Avocado"))
# insert
fruits.insert(2, "banana")
print(fruits)