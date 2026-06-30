def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    small = []
    big = []
    equal = []

    for num in arr:
        if pivot < num:
            big.append(num)
        elif pivot > num:
            small.append(num)
        else:
            equal.append(num)
    
    small_sort = quick_sort(small)
    big_sort = quick_sort(big)

    return small_sort + equal + big_sort

print(quick_sort([1,5,3,2,8,4,4,6,6,6,6,8,8,8,4]))