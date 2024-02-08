a={"apple","orange","cherry","apple"}
print(a)
print(len(a))
print(type(a))
for i in a:
    print(i)
print("apple" in a)
print("onion" in a)
a.add("banana")
print(a)
b={"onion","carrot"}
a.update(b)
print(a)
a.discard("onion")
print(a)
a.discard("onion")
print(a)
z=a.pop()
print(z)
print(a)

x={1,2,3,4,5}
y={6,7,8,9}
w=x.difference(y)
print(w)

x.difference_update(y)
print(x)