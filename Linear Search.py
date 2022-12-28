
def linear(a,key,size):
    flag=0
    for i in range (size):
        if a[i]==key:
            flag=1
            pos=i+1
            break
            
    if flag==1:
        print("Number is found at",pos,"Postion")
    else:
        print("Number Not found")
#main.....................................
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)
key=int(input("Enter Number to be Search:"))
linear(a,key,size)