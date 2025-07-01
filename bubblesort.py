import random
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

mylist = list(range(21))[1:]
print(mylist)
random.shuffle(mylist)
print(bubble(mylist))