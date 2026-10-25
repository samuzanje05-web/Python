def linear_search(arr,target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
        return -1
numbers = [24, 18,37,5, 42,11]
print(linear_search(numbers, 11))
print(linear_search(numbers, 78))