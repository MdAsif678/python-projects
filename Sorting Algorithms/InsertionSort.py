def insertion_sort(arr):
    length = len(arr)

    for i in range(1,length):
        temp = arr[i]
        j = i-1

        while j >= 0 and arr[j] >temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    
    return arr

print(insertion_sort([1,5,4,3,11,9,6,7,5]))