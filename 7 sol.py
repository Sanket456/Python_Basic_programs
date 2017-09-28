string = input()
sml = 0
ll = 0
for i in string:
    if i>='A' and i<='Z':
        ll = ll+1
    elif i>='a' and i<='z':
        sml = sml + 1
print('The number of small letters:',sml)
print('The number of capital letters:',ll)
