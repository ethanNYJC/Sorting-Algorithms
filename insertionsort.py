import random
def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        target = arr[i]
        j = i-1

        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = target

    return arr

mylist = list(range(21))[1:]
random.shuffle(mylist)
print(mylist)
print(insertionsort(mylist))
