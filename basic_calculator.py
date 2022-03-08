"""
Simple Calculator
"""
import sys

while True:
    number_a = float(input("Please enter your first number (X): "))
    number_b = float(input("Please enter your second number (Y): "))
    maths_function = input("Would you like to: (M)ultiply, (D)ivide, (A)dd or (S)ubtract Y from X?: ")
    if maths_function == 'M' or 'm':
        print("The answer to X x Y is: " + str(number_a * number_b))

    elif maths_function == 'D' or 'd':
        print("The answer to X / Y is: " + str(number_a / number_b))

    elif maths_function == 'A' or 'a':
        print("The answer to X + Y is: " + str(number_a + number_b))

    elif maths_function == 'S' or 's':
        print("The answer to X - Y is: " + str(number_a - number_b))

    else:
        print("I do not understand")

    user_restart_answer = input("Would you like to start again? (Y/N): ")
    if user_restart_answer == 'N' or 'n':
        continue
    elif user_restart_answer == 'Y' or 'y':
        break

print("Good bye")
sys.exit