n = int(input("Enter number of members: "))
books = {}
counts = []
for i in range(n):
    name = input("Enter book name: ")
    count = int(input("Enter borrowing count: "))

    books[name] = books.get(name, 0) + count
    counts.append(count)
print("\nAverage borrowing:", sum(counts) / n)
high = max(books.values())
low = min(books.values())
print("\nHighest borrowed book:")
for b, c in books.items():
    if c == high:
        print(b, c)
print("\nLowest borrowed book:")
for b, c in books.items():
    if c == low:
        print(b, c)
print("\nZero borrowing members:", counts.count(0))
freq = {}
for c in counts:
    freq[c] = freq.get(c, 0) + 1
m = max(freq.values())
print("Mode:", [k for k, v in freq.items() if v == m])
