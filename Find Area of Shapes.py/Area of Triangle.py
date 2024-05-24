#Base=float(input('Enter the value of the base of the triangle:')): This line prompts the user to input a value for the base of the triangle. The input() function takes user input as a string, which is then converted to a floating-point number using the float() function and assigned to the variable Base.
Base=float(input('Enter the value of the base of the triangle:'))

#Height=float(input('Enter the value of the height of the triangle:')): This line prompts the user to input a value for the height of the triangle. Similar to the previous input line, it converts the user input to a floating-point number using the float() function and assigns it to the variable Height.
Height=float(input('Enter the value of the height of the triangle:'))

#Area=1/2*(Base*Height): This line calculates the area of the triangle using the formula: Area=1/2×Base×Height. It multiplies the base (Base) by the height (Height), then multiplies by 1/2 . The result is assigned to the variable Area.
Area=1/2*(Base*Height)

#print(Area): This line prints out the calculated area of the triangle. It uses the print() function to display the value stored in the variable Area.
print(Area)
