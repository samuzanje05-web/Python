def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid -1
        else:
            low = mid +1
            return -1
numbers = [5,10, 15, 20, 25, 30]
print(binary_search(numbers, 20))
print(binary_search(numbers, 67))