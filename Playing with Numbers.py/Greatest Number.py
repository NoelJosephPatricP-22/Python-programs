

#Number1 = int(input('Enter the first number:')): This line prompts the user to input the first integer number. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number1.
#Number2 = int(input('Enter the second number:')): This line prompts the user to input the second integer number. Similar to the previous line, it converts the user input to an integer and stores it in the variable Number2.
Number1 = int(input('Enter the first number:'))
Number2 = int(input('Enter the second number:'))

#if Number1 > Number2:: This line checks if Number1 is greater than Number2.
#print('The greatest number is:', Number1): If the condition in the if statement is true (i.e., if Number1 is greater than Number2), this line prints "The greatest number is:" followed by the value of Number1, indicating that Number1 is the greatest.
if Number1 > Number2:
    print('The greatest number is:', Number1)

#else:: If the condition in the if statement is false (i.e., if Number1 is not greater than Number2), the code executes the block under else.
#print('The greatest number is:', Number2): This line prints "The greatest number is:" followed by the value of Number2, indicating that Number2 is the greatest when Number1 is not greater than Number2.
else:
    print('The greatest number is:', Number2)
