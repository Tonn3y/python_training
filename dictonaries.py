# collection of data in key - value pairs.
person = {"name":"Tony","age":19,"religon":"Christian","address":{"city":"Nairobi","street":"Kimathi"},"subjects":["English","Math","Science"]}
print(person["age"])
person["occupation"] = "nurse"
print(person)
# add town to address
person["address"]["town"] = "Nairobi"
print(person)
# add chemistry to subjects
person["subjects"].append("Chemistry")
print(person)
# remove
del person["name"]
print(person)
# keys
print(person.keys())
# values 
print(person.values())
# items - returns key - value pairs
print(person.items())