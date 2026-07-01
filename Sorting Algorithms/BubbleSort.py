def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    
    return arr


my_array = [5, 3, 8, 4,4,4,4, 2]
print(bubble_sort(my_array))