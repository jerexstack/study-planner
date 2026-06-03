import json


try:
    with open("subjects.json", "r") as file:
        study_planner = json.load(file)
except FileNotFoundError:
    study_planner = {}


is_running = True
while is_running:
    print("\n1. Add Subject")
    print("2. View plan")
    print("3. Delete subjects")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = str(input("Enter the subject: "))
        time = int(input("Enter the time to study for in hours: "))
        study_planner[subject] = time
        print("Subject Added!")

    elif choice == "2":
        print("\nStudy Plan:")
        for subject, time in study_planner.items():
            print(f"{subject}:{time}hours")

    elif choice == "3":
        removed_sub = input("Choose a subject to remove: ")
        if removed_sub in study_planner:
            del study_planner[removed_sub]
            print("Subject has been removed")
        else:
            print("Subject is not on list")



    elif choice == "4":
        import json

        file_path = "subjects.json"

        with open(file_path, "w") as file:
            json.dump(study_planner, file, indent=4)
            print("Data has been saved")
        print("Good Bye!")
        is_running = False


    else:
        print("Invalid Choice")


