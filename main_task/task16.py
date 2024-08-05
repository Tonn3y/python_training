# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF.
def grosssalary (a,b) :
    total = a + b
    return total

basicsalary = int(input("Enter basic salary:"))
benefits = int(input("Enter benefits:"))
grosssalary (basicsalary,benefits)

totalsalary = grosssalary(basicsalary,benefits)

def NSSF (d,rate=0.06) :
    if d < 18000 :
        d * rate 
    else :
        return 18000 * rate
    
NSSF = NSSF(totalsalary)
print(NSSF)    