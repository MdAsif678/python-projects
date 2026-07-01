def selection_sort(arr):
    length = len(arr)

    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]
    
    return arr


print(selection_sort([4,10,2,22,3,11,25,32,10]))