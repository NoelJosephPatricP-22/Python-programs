

#Number = int(input('Enter the number:')): This line prompts the user to input an integer. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number.
Number=int(input('Enter the number:'))

#for i in range(1, Number+1):: This line starts a loop that iterates from 1 to the entered number (inclusive). The range() function generates a sequence of numbers starting from 1 and ending at Number. The loop variable i takes on each value in this sequence in each iteration of the loop.
for i in range(1,Number+1):

#if Number % i == 0:: Inside the loop, this line checks if the current value of i is a divisor of Number. The modulus operator % calculates the remainder of the division of Number by i. If the remainder is zero, it means i is a divisor of Number.
  if n%i==0:

#print(i): If i is indeed a divisor of Number, this line prints the value of i. This effectively lists all the divisors of the entered number.
    print(i)
