a=(2,3,4,6,7,8)
print(a)
print(len(a))
print(type(a))
print(a[-1])
print(a[0])
print(a[:3])
if 1 in a:
    print("yes")
else:
    print("no")
print(list(a))
y=list(a)
y[2]=5
print(y)
y.append(23)
print(y)
y.remove(23)
print(y)
print(tuple(y))
x=tuple(y)
del x
#print(x)


A=(2,4,6,8,8,8,10,12)
B=(1,3,5,7,9)
print(A+B)

print(B*2)
for i in A:
    print(i)
for i in range(len(A)):
    print(A[i])
i=0
while i<len(A):   
    print(A[i]) 
    i=i+1
d=A.count(8)
print(d)
q=A.index(10)
print(q)

