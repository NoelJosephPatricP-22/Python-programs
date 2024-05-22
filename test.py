l1=[]
n=int(input("Enter the no of elements"))
for i in range(0,n):
    x=int(input("enter the element:"))
    l1.append(x)
pos1=int(input("Enter the position to be swapped"))
pos2=int(input("Enter the position to be swapped"))
l1[pos1-1],l1[pos2-1]=l1[pos2-1],l1[pos1-1]
print(l1)
