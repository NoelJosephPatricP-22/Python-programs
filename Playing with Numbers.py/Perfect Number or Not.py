
#Number1=int(input('Enter the number:')): This line prompts the user to input an integer number. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number1.
Number1=int(input('Enter the number:'))

#sum=0: This line initializes a variable sum to 0. This variable will be used to accumulate the sum of the factors of the input number.
sum=0

#for i in range(1, n):: This line starts a loop that iterates from 1 to n-1. The range() function generates a sequence of numbers starting from 1 and ending at n-1. The loop variable i takes on each value in this sequence in each iteration of the loop.
for i in range(1,n):
#if n % i == 0:: Inside the loop, this line checks if n (which should be Number1) is divisible by i without leaving a remainder, i.e., if i is a factor of n.  
  if n%i == 0:
#sum=sum+i: If i is indeed a factor of n, its value is added to the variable sum. This accumulates the sum of the factors of n.    
    sum=sum+i

#if sum == n:: After the loop completes, this line checks if the sum of the factors (sum) is equal to the original number (n).
if sum == n:
  print('Perfect Number')

#else:: If the sum of factors is not equal to the original number, the code executes the block under else.
else:
  print('Not  a Perfect Number')
