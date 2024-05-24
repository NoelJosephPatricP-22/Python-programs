

n=int(inpt('Enter the limit:'))

##Initialization: It initializes a variable sum to 0. This variable will be used to accumulate the sum of numbers from 1 to n
sum=0

#Loop: It uses a for loop to iterate over a range of numbers from 1 to n (inclusive).
#range(1, n+1): This generates a sequence of numbers from 1 to n (inclusive). So, if the user inputs 5, range(1, 6) will generate [1, 2, 3, 4, 5].
#i: This variable represents each individual number in the sequence as the loop iterates.
for i in range(1,n+1):
#Accumulation: Inside the loop, it adds each value of i to the sum variable.
#This line accumulates the sum of the numbers from 1 to n.  
  sum=sum+i
print(sum)

#Output: After the loop completes, it prints the final value of the sum variable, which represents the sum of numbers from 1 to n.



