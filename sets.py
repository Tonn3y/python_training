numbers = {1,2,3,4,4,5}
print(numbers)
# add to sets use add method
numbers.add(6)
print(numbers)
# membership in
print(6 in numbers)
# union
x = {"a","b","c"}
y = {"d","e","f"}
z = x.union(y)
print(z)
# intersection
a = {11,12,13,14}
b = {7,8,9,10,11,12,13,14}
c = a.intersection(b)
print(c)
# difference returns elements in the first set that aren't in the second set
a = {11,12,13,14}
b = {7,8,9,10,11,12,13,14}
c = a.difference(b)
print(c)
# symmetric difference.Gives element in a set that aren't common in both sets
a = {11,12,13,14}
b = {7,8,9,10,11,12,13,14}
c = a.symmetric_difference(b)
print(c)
days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
# Remove friday and sunday from the set using methods.
days.remove("friday")
days.remove("sunday")
print(days)
# Add them back to the set
days.add("friday")
days.add("sunday")
print(days)

