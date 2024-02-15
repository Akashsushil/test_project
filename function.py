def sum():
    print("hello akash")
sum()    
def name(firstname,lastname):
    print(firstname+" "+lastname)
name("Akash","susheelan")  
def myfunction(*child): #arbitrary argument
    print("hello "+child[0])  
myfunction("anu","binu","sinu")
def ourfunction(kid1,kid2,kid3):
    print("hello"+" "+kid2) #keyword argument
ourfunction(kid1="anu",kid2="binu",kid3="sinu")
 #arbitrary keywordb argument
def new(**kid):
    print("hello"+" "+kid["lastname"])
new(firstname="anu",lastname="sinu")


fruits=['apple','cherry','grapes','orange']
def food(sweetfruits):
    for i in sweetfruits:
        print(i)
food(fruits )        

def numbers(i):
    return 5*i
print(numbers(5))

def summ(a,b):
    return a+b

a=int(input("enter first no:\n"))
b=int(input("enter second no:\n"))
print(summ(a,b))


numberss=[1,2,3,4,5]
def sum(no):
    sum=0
    for i in no:
        sum=sum+i
    print(sum)
sum(numberss)



