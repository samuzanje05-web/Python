def delete_element(arr,index):
    if 0 <= index < len(arr):
        delete_value = arr[index]
        arr.pop(index)
        return delete_value, arr
    raise IndexError("invalid index")
numbers=[10,20,30,40,]
value, numbers = delete_element(numbers, 1)
print("Deleted:",value)
print("Array:",numbers)
        