def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


arr_shell = [75, 2, 90, 1, 6, 3]
shell_sort(arr_shell)

print("Shell Sort Result:", arr_shell)