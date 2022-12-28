#Quick sort

def quick(a,low,high):   
    if(low<high):
        m=part(a,low,high)
        quick(a,low,m-1)
        quick(a,m+1,high)
def part(a,low,high):
    pivot=a[low]
    i=low+1
    j=high 
    flag=0
    while(not flag):
        while(i<=j and a[i]<=pivot):
            i=i+1
        while(i<=j and a[i]>=pivot):
            j=j-1
            
        if (j<i):
            flag=1
        else:
            t=a[i]
            a[i]=a[j]
            a[j]=t        
    t=a[low]
    a[low]=a[j]
    a[j]=t
    return j
    
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)
    
quick(a,0,size-1)
print("Sorted list is :")
print(a)