# 4. Write a python script to print first N odd natural numbers

n=int(input("Enter the Limit: "))
i=1
while i<=n:
    if i%2!=0:
        print(i,end="  ")
    i=i+1    