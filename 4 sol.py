even = []
odd = []
n = int(input('Enter the number of integers:'))
for i in range(0,n):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
