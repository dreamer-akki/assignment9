#. Write a python script to print first 10 even natural numbers in reverse order


num=int(input("Please enter a limit\n"))
x=num
while x>=0:
    if x%2==0:
        print(x,end=" ")
    x= x-1