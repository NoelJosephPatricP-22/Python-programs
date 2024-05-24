
#Number1=int(input('Enter the first number:')): This line prompts the user to input an integer number. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number1.
Number1=int(input('Enter the first number:'))

#if Number1 > 0:: This line checks if the entered number (Number1) is greater than zero.
#print('The number is positive'): If the condition in the if statement is true (i.e., if Number1 is greater than zero), this line prints "The number is positive".
if Number1>0:
  print('The number is positive')

#else:: If the condition in the if statement is false (i.e., if Number1 is not greater than zero), the code executes the block under else.
#print('The number is negative'): This line prints "The number is negative" if the condition in the if statement is false.
else:
  print('The number is negative')
