def total (a,b,c,d,e) :
    total = a + b + c + d + e
    return total

math = int(input("Maths:"))
english = int(input("English:"))
kiswahili = int(input("Kiswahili:"))
science = int(input("Science:"))
socialstudies = int(input("Socialstudies:"))
total = total(math,english,kiswahili,science,socialstudies)

def average(sum) :
    average = sum/5
    return average
average = average(total)

def grades (a) :
    if a > 79 :
        return ("A")
    elif a >=60 :
        return ("B")
    elif a >= 49 :
        return ("C")        
    elif a >= 40 :
        return ("D")
    elif a >= 0 :
        return ("E")        
    else :
        return ("Error")    

grade = grades(average) 
print(grade)       