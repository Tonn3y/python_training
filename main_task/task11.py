# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
import datetime

# dateofbirth = datetime.datetime(2005,8,31)
# yearofbirth = dateofbirth.year
# monthofbirth = dateofbirth.month
# dateborn = dateofbirth.day


# datetoday = datetime.datetime.now()
# yeartoday = datetoday.year
# monthtoday = datetoday.month
# datetoday = datetoday.day

# # print((yeartoday - yearofbirth),(monthtoday - monthofbirth),(datetodayy - dateborn))

# if yeartoday > yearofbirth :
#     if monthtoday > monthofbirth :
#         print((yeartoday - yearofbirth),(monthtoday - monthofbirth),(datetoday - dateborn))
#     else :
#         print(((yeartoday - yearofbirth) - 1),((monthtoday - monthofbirth) + 12),(datetoday - dateborn))  
#         if datetoday > dateborn :
#               print(((yeartoday - yearofbirth) - 1),((monthtoday - monthofbirth) + 12),(30 + (datetoday - dateborn)))
# else :
#      print("Invalid")  
 
            
datetoday = datetime.datetime.now()
dateborn = input("Enter date born(year/month/day):")
dateborn = dateborn.split("/")
yearborn = int(dateborn[0])
monthborn = int(dateborn[1])
dayborn = int(dateborn[2])
print(dateborn)

years = datetoday.year-yearborn
months = datetoday.month-monthborn
days = datetoday.day-dayborn
                 


if days < 0 :
    if months == 1 :
        months = 12
        years -= 1 
        days += 31
    else :
        months -= 1
        years -= 1
        if months == 3 or 5 or 7 or 8 or 10 or 12 :
            days += 31
        elif months == 4 or 6 or 9 or 11 :
            days += 30
        else :
            if years % 4 == 0 :
               if years % 100 == 0 :
                   if years % 400 == 0 :
                       days += 29
                   else :
                       days += 28
               else :
                    days += 28
            else :
                days += 28

if months < 0 :
    years -= 1
    months += 12        

print(f"years:{years} ,months {months} and days {days}")
