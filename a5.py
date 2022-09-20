# 4. Write a python script to print first N odd natural numbers in reverse order.

n=int(input("Enter the Limit: "))
i=n
while i>0:
    if i%2!=0:
        print(i,end="  ")
    i=i-1    