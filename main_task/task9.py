# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
stars = int(input("Enter number:"))
stars = stars + 1

for star in range(stars):
    star *= "*"
    print(star)