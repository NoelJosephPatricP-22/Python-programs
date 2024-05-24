
#Number = int(input('Enter a number:')): This line prompts the user to input an integer. The input() function takes user input as a string, which is then converted to an integer using the int() function. The entered integer is stored in the variable Number.
Number=int(input('Enter a number:'))

#Sum = 1: This line initializes the variable Sum to 1. This variable will be used to accumulate the factorial value.
Sum=1

#for i in range(1, Number+1):: This line starts a loop that iterates from 1 to the entered number (inclusive). The range() function generates a sequence of numbers starting from 1 and ending at Number. The loop variable i takes on each value in this sequence in each iteration of the loop.
#Sum = Sum * i: Inside the loop, this line multiplies the current value of Sum by i and assigns the result back to Sum. This accumulates the factorial value as the loop iterates through each number from 1 to Number.
for i in range(1,Number+1):
  Sum=Sum*i

#print('Factorial', Sum): After the loop completes, this line prints out the calculated factorial value. It uses the print() function to display the text "Factorial" followed by the value of Sum, which represents the factorial of the input number.
print('Factorial',Sum)

