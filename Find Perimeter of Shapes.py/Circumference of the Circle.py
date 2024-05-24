import math

#Radius = float(input('Enter the radius of the circle:')): This line prompts the user to input a value for the radius of the circle. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function and assigned to the variable Radius.
Radius=float(input('Enter the radius of the circle:'))

#Circumference = 2 * math.pi * Radius: This line calculates the circumference of the circle using the formula for the circumference: 2×𝜋×Radius Here, the value of 𝜋π is approximated as 3.14. The result is assigned to the variable Circumference. Circumference=2*3.14*Radius

#print('Circumference of the circle is:', Circumference): This line prints out the calculated circumference of the circle. It uses the print() function to display the text "Circumference of the circle is:" followed by the value of the Circumference variable.
print('Circumference of the circle is:',Circumference)
