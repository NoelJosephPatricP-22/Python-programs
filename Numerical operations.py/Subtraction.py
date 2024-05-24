#number1 = float(input('Enter the first number:')): This line prompts the user to enter the first number. The input() function takes the user's input as a string, and float() converts it into a floating-point number to allow for decimal input. The entered value is then stored in the variable number1.
Number1 = float(input('Enter the first number:'))
#number2 = float(input('Enter the second number:')): Similar to the previous line, this line prompts the user to enter the second number, converts it into a floating-point number, and stores it in the variable number2.
Number2 = float(input('Enter the second number:'))

#subtract = number1 - number2: This line calculates the sum of the two numbers entered by the user and stores the result in the variable subtract. However, the variable name subtract is misleading because it's storing the sum, not the difference
Subtract = Number1 - Number2

#print('difference of two numbers:', subtract): This line prints the sum of the two numbers. The text "difference of two numbers:" is displayed followed by the value stored in the variable subtract, which, as mentioned earlier, is actually the sum, not the difference.
print('difference of two numbers:', Subtract)
