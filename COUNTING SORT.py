#COUNTING SORT
size=int(input("Enter size of list:"))
a=[]
i=0
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)
    
size=len(a)
result=[0]*size
count=[0]*10
i=0
for i in range(size):
    count[a[i]]+=1
for i in range(1,10):
    count[i]=count[i]+count[i-1]
    
i=size-1
while i>=0:
    result[count[a[i]]-1] = a[i]
    count[a[i]]-=1
    i=i-1
for i in range(0,size):
    a[i]=result[i]
    
print("Sorted list is :")
print(a)