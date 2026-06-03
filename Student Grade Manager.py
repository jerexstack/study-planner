import json


try:
    with open("json.students", "r") as file:
        Grade_manager = json.load(file)
except FileNotFoundError:
    Grade_manager = {}

is_running = True

while is_running:
    print("\n 1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. View average score")
    print("6. Exit")

    choice = input("Enter an option: ")

    if choice == "1":
        student = input("Enter student's name: ")
        subject = input("Enter student's subject: ")
        score = input("Enter student's score: ")
        Grade_manager[student] = {
            "subject": subject,
            "score": int(score)
        }

    elif choice == "2":
        print("_____ Student's Grades_____")
        for student, data in Grade_manager.items():
            print(f"Student: {student}")
            print(f"Subject:{data['subject']} ")
            print(f"Score: {data['score']}")


    elif choice == "3":
        search = input("Enter student's name: ")
        if search in Grade_manager:
            data = Grade_manager[search]
            print(f"Student: {search}")
            print(f"Subject: {data['subject']}")
            print(f"score: {data['score']}")

        else:
            print("Student does not exist")

    elif choice == "4":
        removed_stud = input("Enter student's name: ")
        if removed_stud in Grade_manager:
            Grade_manager.pop(removed_stud)
            print("Student has been removed!")
        else:
            print("Student has not been found")


    elif choice == "5":
        total = 0
        for student in Grade_manager.values():
            total += student["score"]
        average = total / len(Grade_manager)
        print(f"Your total average is {average}")

    elif choice == "6":
        file_path = "json.students"
        with open(file_path, "w") as file:
            json.dump(Grade_manager, file, indent=4)
        print("Grade has been saved")
        print("Good Bye")
        is_running = False

    else:
        print("Invalid option")















