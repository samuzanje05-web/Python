def insert_element(arr, index,value):
    if 0 <= index <= len(arr):
     arr.insert(index, value)
    return arr
numbers =[10,20,30,40]
numbers = insert_element(numbers,2,35)
print(numbers)
    