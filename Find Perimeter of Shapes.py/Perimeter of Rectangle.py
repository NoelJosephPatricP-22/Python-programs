
#Length=float(input('Enter the length of the rectangle:')): This line prompts the user to input a value for the length of the rectangle. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function and assigned to the variable Length.
Length=float(input('Enter the length of the rectangle:'))

#Breadth=float(input('Enter the breadth of the rectangle:')): This line prompts the user to input a value for the breadth of the rectangle. Similar to the previous input line, it converts the user input to a floating-point number using the float() function and assigns it to the variable Breadth.
Breadth=float(input('Enter the breadth of the rectangle:'))

#perimeter=2*(Length+Breadth): This line calculates the perimeter of the rectangle using the formula: Perimeter=2×(Length+Breadth). It adds the length (Length) and breadth (Breadth) of the rectangle, multiplies the sum by 2, and assigns the result to the variable Area.
Perimeter=2*(Length+Breadth)

#print('Perimeter of the rectangle is:',Perimeter): This line prints out the calculated perimeter of the rectangle. It uses the print() function to display the text "Perimeter of the rectangle is:" followed by the value of the Area variable.
print('Perimeter of the rectangle is:',Perimeter)
