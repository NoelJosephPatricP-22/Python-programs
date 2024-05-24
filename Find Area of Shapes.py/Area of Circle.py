import math

#Radius=float(input('Enter the radius:')): This line prompts the user to enter the radius of a circle. The input() function takes input from the user, and whatever the user types is treated as a string. Then, float() converts this string into a floating-point number, which allows for decimal input. The entered radius is stored in the variable r
Radius=float(input('Enter the radius:'))

#area=math.pi*Radius*Radius: This line calculates the area of a circle using the formula 𝜋×𝑟^, where 𝜋 is approximately 3.14 and r is the radius entered by the user. The result is stored in the variable area.
Area=math.pi*Radius*Radius

#print('\nArea of circle is:',area): This line prints the calculated area of the circle. The \n in the string adds a newline character, so the output starts on a new line. Then, it prints "Area of circle is:" followed by the value stored in the variable area.
print('\nArea of circle is:',Area)

