import random
def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            return arr

    return arr

mylist = list(range(21))[1:]
random.shuffle(mylist)
print(mylist)
print(bubblesort(mylist))
