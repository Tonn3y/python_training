# assignment
myname = "JOHn "
newname = myname.lower()
print(newname)

sentence_one = "The Dog Breed is German Shepherd"
sentence_one = sentence_one[8:23]
print(sentence_one)

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces"
newsentencetwo = sentence_two[16:30]
print(sentence_two)

sentence_three = "The lazy dog; ran so fast; it hit the wall."
sentence_three = sentence_three.split(';')
print(len(sentence_three))

first_name = "Joh.n"
last_name = "Do,e"
first_name = first_name.replace(".","")
last_name = last_name.replace(",","")
fullname = first_name + " " + last_name
print(fullname)

r = '["E","W","C"]'
newr = r.replace("[","").replace("]","").replace('"',"").replace(",","")
print(newr)