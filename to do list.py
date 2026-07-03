tasks = ["cleaning", "laundry", "dishes", "eating", "sleeping"]

while True:
    print(tasks)

    choice = input("Add, Remove, or Exit: ").lower()

    if choice == "add":
        tasks.append(input("Task: "))

    elif choice == "remove":
        task = input("Task to remove: ")
        if task in tasks:
            tasks.remove(task)

    elif choice == "exit":
        break