
#Number = int(input('Enter the number to display its multiples:')): This line prompts the user to input an integer. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number.
Number=int(input('Enter the number to display its multiples:'))

#for i in range(1, 11):: This line starts a loop that iterates from 1 to 10 (inclusive). The range() function generates a sequence of numbers starting from 1 and ending at 10 (but not including 11). The loop variable i takes on each value in this sequence in each iteration of the loop.
#print(Number,'×',i,'=',Number*i): Inside the loop, this line prints the multiplication table for the input number. It displays the current value of Number, followed by the multiplication symbol (×), then i, followed by an equal sign (=), and finally the product of Number and i, which gives the multiples of Number up to 10.
for i in range(1,11):
  print(Number,'×',i,'=',Number*i)
  
