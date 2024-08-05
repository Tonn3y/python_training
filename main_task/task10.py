# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [["omo","30kshs","300"], ["milk","50kshs","200"],["bread","45ksh","359"], ["coffee","5kshs","79"]]
totalstock = 0

for stock in prods :
    totalstock += int(stock[2])

print(totalstock)