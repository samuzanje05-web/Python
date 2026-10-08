# write a program to find whether the list contain duplicates
def check_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                print("Duplicate found:", numbers[i])
                return True
            else:
                if numbers[i] != numbers[j]:
                    print("Not duplicate:", numbers[i], numbers[j])

    return False


numbers = [10, 20, 30, 20, 40]

if check_duplicate(numbers):
    print("Duplicate numbers found")
else:
    print("No duplicate numbers")
        
   