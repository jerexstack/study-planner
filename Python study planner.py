study_planner = {}

is_running = True
while is_running:
    print("\n1. Add Subject")
    print("2. View plan")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("Enter the subject: ")
        time = input("Enter the time: ")
        study_planner[subject] = time
        print("Subject Added!")
    elif choice == "2":
        print("\nStudy Plan:")
        for subject, time in study_planner.items():
            print(f"{subject}:{time}")
    elif choice == "3":
        print("Good Bye!")
        is_running = False

    else:
        print("Invalid Choice")
