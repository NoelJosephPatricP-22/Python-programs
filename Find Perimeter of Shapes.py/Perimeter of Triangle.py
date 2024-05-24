
#Side1=float(input('Enter the value of the first side of the triangle:')): This line prompts the user to input a value for the first side of the triangle. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function and assigned to the variable Side1.
Side1=float(input('Enter the value of the first side of the triangle:'))

#Side2=float(input('Enter the value of the second side of the triangle:')): This line prompts the user to input a value for the second side of the triangle. Similar to the previous input line, it converts the user input to a floating-point number using the float() function and assigns it to the variable Side2.
Side2=float(input('Enter the value of the second side of the triangle:'))

#Side3=float(input('Enter the value of the third side of the triangle:')): This line prompts the user to input a value for the third side of the triangle. Similar to the previous input lines, it converts the user input to a floating-point number using the float() function and assigns it to the variable Side3.
Side3=float(input('Enter the value of the third side of the triangle:'))

#Perimeter=Side1*Side2*Side3: This line incorrectly calculates the product of the three sides. The perimeter of a triangle is the sum of the lengths of its three sides, not the product. So, this line should be modified to Perimeter = Side1 + Side2 + Side3.
Perimeter=Side1+Side2+Side3

#print('Perimeter of the triangle is:',Perimeter): This line prints out the calculated perimeter of the triangle. It uses the print() function to display the text "Perimeter of the triangle is:" followed by the value of the Perimeter variable.
print('Perimeter of the triangle is:')

