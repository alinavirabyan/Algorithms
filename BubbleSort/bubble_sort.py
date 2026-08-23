def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr_bubble = [-7, -2, 9, 1, -6, 3]
bubble_sort(arr_bubble)

print("Bubble Sort Result:", arr_bubble)