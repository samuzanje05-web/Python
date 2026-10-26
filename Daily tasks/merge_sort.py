def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[0] <= right[0]:
        return left + right
    else:
        return right + left


numbers = [4, 2]
print(merge_sort(numbers))