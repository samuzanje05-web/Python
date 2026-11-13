queue = []
while True:
    print("\n--- Event Processing System ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        event = input("Enter event name: ")
        queue.append(event)
        print("Event added successfully!")
    elif ch == 2:
        if queue:
            print("Processing Event:", queue.pop(0))
        else:
            print("No events to process!")
    elif ch == 3:
        if queue:
            print("Pending Events:", queue)
        else:
            print("No pending events!")
    elif ch == 4:
        event = input("Enter event to cancel: ")
        if event in queue:
            queue.remove(event)
            print("Event cancelled successfully!")
        else:
            print("Event not found!")
    elif ch == 5:
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")
