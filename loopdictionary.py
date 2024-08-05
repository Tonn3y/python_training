person = {
    "name":"Tony",
    "age":19,
    "city":"Nairobi",
    "location":"Kenyatta avenue"
}

for key,value in person.items():
    print(f"{key}:{value}")

for value in person.values():
    print(f"{value}")   

person1 = {
    "name":"Tony",
    "age":19,
    "city":"Nairobi",
    "location":"Kenyatta avenue"
}
person2 = {
    "name":"Barbara",
    "age":19,
    "city":"Imaara",
    "location":"Imaara mall"
}     

for (key,value), (key1,value1) in zip(person1.items(),person2.items()):
    print(key,value)
    print(key1,value1)

fruits = ["Orange","banana","Melons"]
colors = ["lime","yellow","red"]

for fruit,color in zip(fruits,colors):
    print(fruit, "is", color)