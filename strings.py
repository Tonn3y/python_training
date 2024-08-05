firstname = "Tony"
secondname = "Kibet"
space = " "
fullnames = firstname + space + secondname
age = 25
age = str(age)

print(fullnames[5:10])
upper = fullnames.upper()
print(upper)
f2 = upper.lower()
print(f2)
f3 = f2.capitalize()
print(f3)
f4 = f3.islower
choice = "     Novermber intake         "
print(len(choice))
choiceresult = choice.strip()
print(len(choiceresult))
secondname = secondname.replace("Kibet","Kemboi")
print(fullnames)
# split
names = "arnold:tony:pendo"
print(names.split(':'))
# count
sidemen = "jj olatunji"
print(sidemen.count(" "))
# concat
# fname = "Alvin"
# lname = "Okemwa"
# combined = fname.concat(lname)
