"""
Simple Calculator
"""
import sys

while True:
    number_a = float(input("Please enter your first number (X): "))
    number_b = float(input("Please enter your second number (Y): "))
    maths_function = input("Would you like to: (M)ultiply, (D)ivide, (A)dd or (S)ubtract Y from X?: ")

    # One straightforward fix would be to be explicit in the conditional.
    if maths_function == 'M' or maths_function == 'm':
        print("The answer to X x Y is: " + str(number_a * number_b))

    # You could also create a small list on the go and check whether the character is
    # in that list.
    elif maths_function in ['D', 'd']:
        print("The answer to X / Y is: " + str(number_a / number_b))

    # My preferred way of doing it would be to take the input and "clean" it before
    # doing the comparison. In this case, you would simply cast whatever the user put in
    # to lowercase. That way you know exactly what you're comparing and don't have to
    # worry about lower/uppercase.
    elif maths_function.lower() == 'a':
        print("The answer to X + Y is: " + str(number_a + number_b))

    elif maths_function.lower() == 's':
        print("The answer to X - Y is: " + str(number_a - number_b))

    else:
        print("I do not understand")

    user_restart_answer = input("Would you like to start again? (Y/N): ")
    if user_restart_answer.lower() == 'n':
        continue
    elif user_restart_answer.lower() == 'y':
        break

print("Good bye")
# sys.exit is a function that needs to be called by adding the parentheses, otherwise
# the statement has no effect. However, there's no need to explicitly tell python to
# exit here, since it terminates once it has reached the end of the file.
sys.exit()
