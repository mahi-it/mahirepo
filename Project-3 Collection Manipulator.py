
print("Welcome to the Student Data Organizer!")
students = []

while True:
    print()
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print()
            print("Enter student details:")

            s_id = int(input("Student ID: "))

            duplicate = False

            for student in students:
                if student["student_tuple"][0] == s_id:
                    duplicate = True
                    break

            if duplicate:
                print("Student ID already exists!")

            else:
                name = input("Name: ")
                age = int(input("Age: "))
                grade = input("Grade: ")
                DOB = input("Date of Birth (YYYY-MM-DD): ")

                subjects = set(input("Subjects (comma-separated): ").split(",") )

                student_tuple = (s_id, DOB)

                student = {
                    "student_tuple": student_tuple,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "subjects": subjects,
                }

                students.append(student)

                print("Student added successfully!")

        case 2:
            print()
            if len(students) == 0:
                print("No student record found!")

            else:
                print("--- Display All Students ---")

                for student in students:
                    print(
                        f"Student ID: {student['student_tuple'][0]} | "
                        f"Name: {student['name']} | "
                        f"Age: {student['age']} | "
                        f"Grade: {student['grade']} | "
                        f"Subjects: {','.join(student['subjects'])}"
                    )

                print()
                print("Total Students:", len(students))

        case 3:
            print()
            print("--- Updating Student Information ---")

            var = int(input("Enter Student ID: "))

            for student in students:

                if student["student_tuple"][0] == var:

                    print("1. Student ID")
                    print("2. Name")
                    print("3. Age")
                    print("4. Grade")
                    print("5. DOB")
                    print("6. Subjects")

                    update = int(input("What do you want to update? "))

                    if update == 1:
                        print(
                            "Student ID is immutable and cannot be changed."
                        )

                    elif update == 2:
                        student["name"] = input("Enter new name: ")
                        print("Name updated successfully!")

                    elif update == 3:
                        student["age"] = int(input("Enter new age: "))
                        print("Age updated successfully!")

                    elif update == 4:
                        student["grade"] = input("Enter new grade: ")
                        print("Grade updated successfully!")

                    elif update == 5:
                        print(
                            "DOB is immutable and cannot be changed."
                        )

                    elif update == 6:
                        student["subjects"]=set( input("Enter new subjects: ").split(",")
                        )
                        print("Subjects updated successfully!")

                    else:
                        print("Invalid choice.")

                    break

            else:
                print("Student ID not found!")

        case 4:
            print()
            print("--- Delete Student ---")

            var = int(input("Enter Student ID you want to delete: ") )

            for student in students:

                if student["student_tuple"][0] == var:

                    del students[students.index(student)]

                    print("Student with ID %d deleted successfully!" % var)

                    break

            else:
                print("Student ID not found.")

        case 5:
            print()
            print("--- Subjects Offered ---")

            if len(students) == 0:
                print("No student records found!")

            else:
                for student in students:
                    print("student_ID",student["student_tuple"][0],":",",".join(student["subjects"]))

        case 6:
            print()
            print("Thanks for using Student Data Organizer and displaying the exit message!" )
            break

        case _:
            print("Invalid choice")