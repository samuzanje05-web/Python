n = int(input("Enter number of employees: "))

salary = []
for i in range(n):
    s = float(input("Enter salary: "))
    salary.append(s)

a = salary.copy()

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print("\nSelection Sort:", a)
print("Top 5 Salaries:", a[-5:][::-1])

b = salary.copy()

for i in range(n):
    for j in range(n - i - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

print("\nBubble Sort:", b)
print("Top 5 Salaries:", b[-5:][::-1])
