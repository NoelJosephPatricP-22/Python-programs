
#Number=int(input('Enter the first number:')): This line prompts the user to input an integer number. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number.
Number=int(input9'Enter the first number:'))

#if Number % 2 == 0:: This line checks if the entered number (Number) is divisible by 2 without leaving a remainder. If the remainder after dividing Number by 2 is 0, it means that Number is an even number.
if Number%2==0:
  print('The number is even')

#else:: If the condition in the if statement is false (i.e., if Number is odd), the code executes the block under else.
else:
  print('The number is odd')
