
T = (1,2,3,4,5)
print('Original Tuple is :',end=' ')
print(T)
l=[]
for i in T:
    if T.index(i)%2==1:
        l.append(i)
T2 = tuple(l)
print('Values at Odd index are',end=' ')
print(T2)
