correct_password = "1234"

for attempt in range(3):

    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break

    else:
        print("Incorrect Password")

else:
    print("Account Locked")