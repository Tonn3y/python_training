# quiz
my_ds = [23,"Jane",(560),["Lesson","Maths",{"Currency":"KES"}],987,(76,"John")]
# 1. Print KES
print(my_ds[3][2]["Currency"])
# 2. Print 560
print(my_ds[2])
# 3. Print Maths
print(my_ds[3][1])
# In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["Amount"] = 90
print(my_ds)
# Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
my_ds[4] = 789
print(my_ds)
# 6. Change the name “John” to “Jane” . 
my_ds[5] = list(my_ds[5])
my_ds[5][1] = "Jane"
my_ds = tuple(my_ds[5])
print(my_ds)