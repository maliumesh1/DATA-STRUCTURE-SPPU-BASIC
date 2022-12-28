#!/usr/bin/python3
def sentinelSearch(arr, n, key):
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
 
    while (arr[i] != key):
        i += 1
    arr[n - 1] = last
 
    if ((i < n - 1) or (arr[n - 1] == key)):
        print(key, "is present at index", i)

    else:
        print("Element Not found")
# Driver code
arr = [10, 20, 180, 30, 60, 50, 110, 100, 70]
n = len(arr)
key = 20
sentinelSearch(arr, n, key)