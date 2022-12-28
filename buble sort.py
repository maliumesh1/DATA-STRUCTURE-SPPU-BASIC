
#BUBBLE SORT
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)

for i in range(size):
    for j in range (0,size-i-1):
        if a[j]>a[j+1]:#j मोठा असेल j+1 पेक्षा तरच loop फिरेल
            t=a[j] #t मध्ये पहिली value save होणार
            a[j]=a[j+1] #j ,j+1 value Exchange होणार
            a[j+1]=t    #j ची Value t मध्ये save होणार
print("Sorted list is :")
print(a)






