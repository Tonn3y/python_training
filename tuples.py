#tuples are immutable i.e can not be changed.
students = ("Tony","Andrew","Barbra","Stanley")
print(students[2:])
# tuple => converts any data structure into a tuple.
x = [1,2,3,4,5]
x = tuple(x)
print(type(x))

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
# Question 1
print(days[2])
# Question 2
print(len(days))
# Question 3
days = list(days)
days[3] = "Thur"
days = tuple(days)
print(days)