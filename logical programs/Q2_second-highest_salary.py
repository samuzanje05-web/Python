highest_salary = 0
second_highest = 0

for i in range(5):
    salary = float(input("Enter salary: "))
    if salary > highest_salary:
        second_highest = highest_salary
        highest_salary = salary
    elif salary > second_highest:
        second_highest = salary

print("Highest salary:", highest_salary)
print("Second highest salary:", second_highest)
