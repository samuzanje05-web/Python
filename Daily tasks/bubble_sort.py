def bubble_sort(arr):
    n= len(arr)
    for pass_number in range( n - 1):
        swapped = False
        for i in range(n - pass_number - 1):
            if arr[i] > arr [i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
                 break
    return arr
numbers = [29, 10, 14, 37,13]
print(bubble_sort(numbers))