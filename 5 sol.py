words=[]
mx = 0
n = int(input('Enter the Number of Entries to be made:'))
for i in range(0,n):
    char = input()
    words.append(char)
    length = int(len(char))
    if length>mx:
        mx=length
        ans=char
print('Maximum length of string:')
print(mx,ans)
