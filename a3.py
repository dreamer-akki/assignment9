# 3. Write a python script to print first N natural numbers in reverse order

n=int(input("Enter the Limit: "))
i=1
while i<=n:
    print(n-i,end=" ")
    i += 1
print()