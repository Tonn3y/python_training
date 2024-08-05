def grosssalary (a,b) :
    total = a + b
    return total

basicsalary = int(input("Enter basic salary:"))
benefits = int(input("Enter benefits:"))
grosssalary (basicsalary,benefits)

totalsalary = grosssalary(basicsalary,benefits)

def NHIF (c) :
    if c <= 5999:
        return 150
    elif c >= 6000 and c <= 7999 :
        return 300
    elif c >= 8000 and c <= 11999 :
        return 400
    elif c >= 12000 and c <= 14999 :
        return 500
    elif c >= 15000 and c <= 19999 :
        return 600
    elif c >= 20000 and c <= 24999 :
        return 750
    elif c >= 25000 and c <= 29999 :
        return 850
    elif c >= 3000 and c <= 34999 :
        return 900
    elif c >= 35000 and c <= 39999 :
        return 950
    elif c >= 40000 and c <= 44999 :
        return 1000
    elif c >= 45000 and c <= 49999 :
        return 1100
    elif c >= 50000 and c <= 59999 :
        return 1200
    elif c >= 60000 and c <= 69999 :
        return 1300
    elif c >= 70000 and c<= 79999 :
        return 1400
    elif c >= 80000 and c <= 89999 :
        return 1500
    elif c >= 90000 and c <= 99999 :
        return 1600
    elif c >= 100000 :
        return 1700
    else :
        return ("Error")
NHIF = NHIF(totalsalary)
print(NHIF)    