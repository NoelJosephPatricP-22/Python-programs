
#Input: The code prompts the user to input three numbers, which are then stored in variables Number1, Number2, and Number3 respectively using the input() function. These inputs are converted to integers using the int() function.
Number1=int(input('Enter the first number:'))
Number2=int(input('Enter the second number:'))
Number3=int(input('Enter the third number:'))

#Comparison: The code then compares the three numbers using if, elif, and else statements to determine which one is the greatest.
#If Number1 is greater than both Number2 and Number3, it prints that Number1 is the greatest.
#If Number2 is greater than both Number1 and Number3, it prints that Number2 is the greatest.
#If neither of the above conditions is true, it means Number3 is the greatest, so it prints that Number3 is the greatest.
if (Number1>Number2) & (Number1>number3):
  print('The greatest number is:',Number1)

elif(Number2>Number1) & (Number2>Number3):
  print('The greatest number is:',Number2)

else:
  print('The greates number id:',Number3)
#Output: Finally, the code prints the result indicating which number is the greatest.  
