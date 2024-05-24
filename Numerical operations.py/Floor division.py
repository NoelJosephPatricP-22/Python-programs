'''Floor division is a division operation that rounds the result down to the nearest whole number or integer, which is less than or equal to the normal division result'''

#number1=float(input('Enter the fisrt number:')): This line prompts the user to enter the first number. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function to allow for decimal input. The entered value is stored in the variable number1.
Number1=float(input('Enter the fisrt number:'))

#number2=float(input('Enter the second number:')): Similar to the previous line, this line prompts the user to enter the second number. The input is converted to a floating-point number and stored in the variable number2.
Number2=float(input('Enter the second number:'))

#floordivision=number1//number2: This line calculates the floor division of number1 by number2 and stores the result in the variable floordivision
Floordivision=Number1//Number2

#print('Division of number1 by number2:',floordivision): Finally, this line prints out the result of the floor division. It displays a message 'Division of number1 by number2:' followed by the value of floordivision.
print('Floor Division of number1 by number2:',Floordivision)
