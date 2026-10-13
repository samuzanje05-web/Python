def count():
    count = 1

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = count()
print(c())
print(c())
print(c())
print(c())
