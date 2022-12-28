#!/usr/bin/python3



def bs(array, x, low, high):
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array=[4,7,8,9,28,67]
'''//n=int(input("enter the length: " ) )
//for i in range (n):
    //element=float(input("input element: "))
    //array.append(element)
x = //int(input("Enter The Element to Find:"))'''
x=28
result = bs(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")