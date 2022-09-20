# 6. Write a python script to print first N even natural numbers

Number=int(input("Enter the Limit: "))
i=1
while i<=Number:
    if i%2==0:
        print(i,end=" ")
    i+=1