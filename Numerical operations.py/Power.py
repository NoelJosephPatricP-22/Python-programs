#power_value=float(input('Enter the fisrt number:')): This line prompts the user to enter the first number. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function to allow for decimal input. The entered value is stored in the variable number1.
Power_value=float(input('Enter  the power:'))

#number1=float(input('Enter the fisrt number:')): This line prompts the user to enter the first number. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function to allow for decimal input. The entered value is stored in the variable number1.
Number1=float(input('Enter the number:'))

#Calculate the power of any number of your entered choice
Power=Number1**Power

# This line prints out the calculated power. It uses the print() function to display the text "The answer is:" followed by the value of the variable Power.
print('The answer is:',Power)
