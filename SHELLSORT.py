#SHELLSORT
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)

d=size//2
while d>0:
    for i in range (d,size):
        t=a[i]
        j=i 
        while(j >= d and a[j-d] > t):
            a[j]=a[j-d]
            j-=d
        a[j]=t
    d=d//2
print("Sorted list is :")
print(a)