
#Input: The code prompts the user to enter a number. The input() function reads the input as a string, which is then converted to an integer using the int() function. The entered number is stored in the variable Number1.
Number1=int(input('Enter the Number:'))

#Square Root Calculation: It calculates the square root of the entered number using the exponentiation operator **. In Python, raising a number to the power of 1/2 calculates its square root.
SquareRoot=(Number1)**(1/2)

#Print: It prints the square root using an f-string (formatted string) to embed the value of Number1.
#The f'Square Root of {Number1} is:' part of the print statement is a formatted string that allows us to insert the value of Number1 into the string. The value of SquareRoot is then printed next to this string.
print(f'Square Root of {Number1} is:',SquareRoot)
