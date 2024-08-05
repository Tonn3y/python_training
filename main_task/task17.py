# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

def grosssalary (a,b) :
    total = a + b
    return total

basicsalary = int(input("Enter basic salary:"))
benefits = int(input("Enter benefits:"))
grosssalary (basicsalary,benefits)

totalsalary = grosssalary(basicsalary,benefits)

def NHDF (e) :
    return 0.015 * e

NHDF = NHDF(totalsalary)
print(NHDF)
