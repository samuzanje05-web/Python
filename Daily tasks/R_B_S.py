def B_S_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid =(low+high)
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return B_S_recursive(arr, target low, mid-1)
    else:
        return B_S_recursive(arr, target, mid + 1, high)
numbers =[5,11,18,24,31,42,56]
print(B_S_recursive(numbers, 42,0,len(numbers)-1))