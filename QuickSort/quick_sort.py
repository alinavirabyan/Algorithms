def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


arr_quick = [73, 2, 9, -1, 6, 3]
sorted_arr_quick = quick_sort(arr_quick)

print("Quick Sort Result:", sorted_arr_quick)