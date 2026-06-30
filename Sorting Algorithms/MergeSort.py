def merge(arr1,arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return merge(left_sort,right_sort)

print(merge_sort([1,2,3,4,3,2,1,9,23,12,43,532]))