def binary(a,key,size):
    i=0
    j=size-1
    flag=0
    
    while i<=j and flag==0:
        mid=(i+j)//2
        
        if a[mid]==key:         
            pos=mid+1
            flag=1
            
        if a[mid]<key:
            i=mid+1
            
        if a[mid]>key:
            j=mid-1
            
       
    if flag==1:
        print ("Number found at" ,pos,"position")  
    else:
        print ("Number Not found ")
#main....................................
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)
key=int(input("Enter Number to be Search:    "))
binary(a,key,size)