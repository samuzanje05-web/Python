def append_element(arr, value):
    arr.append(value)
    return arr
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
number= [1,2,3,4]
number = append_element(number,5)
print(number)
print(linear_search(number, 3))
print(linear_search(number,7))
        