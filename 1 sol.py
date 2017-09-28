items = []
n = int(input())
#while len(items) < n:
for s in range(0,n):
    i = int(input("Enter the data:"))
    items.append(i)
print (items)
print(sum(items)/n)
