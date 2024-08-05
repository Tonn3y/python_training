# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# If the number is a multiple of 4, print out “divisible by 4”.

# number = int(input("Enter a number:"))
# if number % 2 == 0 and number % 4 == 0:
#     print(f"{number} is divisible by 4")
# elif number % 2 == 0 :
#         print("Even")
# else:
#     print("Odd")   


def divisibility() :
    number = int(input("Enter a number:"))
    if number % 2 == 0 and number % 4 == 0:
       print(f"{number} is even and divisible by 4")
    elif number % 2 == 0 :
        print("Even")
    else:
       print("Odd")

divisibility()       