present = 0
absent = 0

for i in range(18):

    day = input("Enter attendance (p/a): ")

    if day == "p":
        present = present + 1
    else:
        absent = absent + 1

total_days = present + absent

attendance_percentage = (present / total_days) * 100

print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(attendance_percentage, 2), "%")

if attendance_percentage >= 75:
    print("Bonus: Eligible")
else:
    print("Bonus: Not Eligible")