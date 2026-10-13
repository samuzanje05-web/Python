low_risk_count = 0
medium_risk_count = 0
high_risk_count = 0

for i in range(10):

    amount = float(input("Enter transaction amount: "))

    if amount < 5000:
        low_risk_count = low_risk_count + 1
        print("Low Risk")

    elif amount < 50000:
        medium_risk_count = medium_risk_count + 1
        print("Medium Risk")

    else:
        high_risk_count = high_risk_count + 1
        print("High Risk")

print("Low Risk:", low_risk_count)
print("Medium Risk:", medium_risk_count)
print("High Risk:", high_risk_count)
