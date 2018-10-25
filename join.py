n = input('Enter A String:')
a = list(n)
b = []
for i in a:
    if i==' ':
        continue
    else:
        b.append(i)
print(''.join(b))

