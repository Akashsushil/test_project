num=int(input("enter the number:"))
if (num%2==0):
    print('even')
else:
    print('odd')

list2=[]
list3=[]
list1=[10,15,20,25,30,35,40]
for i in list1:
    if i%2==0:
        list2.append(i)
    else:
       list3.append(i)
print(list2,list3)


x=0
y=0
for i in list1:
    if i%2==0:
        list2.append(i)
        x=x+1
    else:
       list3.append(i)
       y=y+1

print(x)
print(y)













        

