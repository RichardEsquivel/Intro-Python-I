# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
# I implemented a type check to confirm that the characters entered in where all digits if not if gives the else error message.
if num.isdigit() is True:
    num = int(num)

    if num % 2 == 0:
        print("Even!")
    if num % 2 == 1:
        print("Odd!")
else:
    print("You didn't type a number try again!")
