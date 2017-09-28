n = int(input('Enter the Number:'))
c=0
while n!=0:
    b=n%10
    n=n//10
    c=c*10+b
print(c)
