#data structures
fruits=["apple","orange","mango","banana","berry","grapes"]
print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[1])
print(fruits[-1])
print(fruits[2:5])
if "mango" in fruits:
    print("yes")
else:
    print("no")
fruits[1]="lime" #replace
print(fruits)
fruits[0:2]="kiwi","watermelon"
print(fruits)


fruits.insert(2,"avacado") #insert
print(fruits)
print(len(fruits))
fruits.insert(3,"strawberry")
print(fruits)
print(len(fruits))


fruits.append("greenapple") #append
print(fruits)

vegetables=["carrot","potatto","onion","beans"] #extend two list
fruits.extend(vegetables)
print(fruits)
print(len(fruits))
fruits.remove("greenapple") #remove an element from list
print(fruits)

fruits.pop(3) #remove based on index
print(fruits)

fruits.pop()
print(fruits) #remove last element
 
del fruits[-1]
print(fruits)
fruits.clear()
print(fruits)



#list2=[2,4,5,6,8,9]
#for i in list2:
    #print(i)
#for i in range(len(list2)):
 #print(list2[i])



list3=["arm","leg","ears","eyes"]
i=0
while i<len(list3): #whileloop
   print(list3[i])
   i=i+1










