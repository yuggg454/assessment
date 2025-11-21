class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1  
        
    def new_admission(self):
        print("\n--- New Student Admission ---")
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        student_class = int(input("Enter class (1-12): "))
        mobile = input("Enter guardian mobile number: ")

        if age < 5 or age > 18:
            print("Age must be between 5 and 18.")
            return

        if len(mobile) != 10 or not mobile.isdigit():
            print("Mobile number must be 10 digits.")
            return

        if student_class < 1 or student_class > 12:
            print("Class must be between 1 and 12.")
            return

        student_id = self.next_id
        self.next_id += 1

        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }

        print(f"Admission successful! Assigned Student ID: {student_id}")

    def view_student(self):
        print("\n--- View Student Details ---")
        student_id = int(input("Enter student ID: "))

        if student_id in self.students:
            data = self.students[student_id]
            print("\nStudent Found:")
            print(f"Name : {data['name']}")
            print(f"Age  : {data['age']}")
            print(f"Class: {data['class']}")
            print(f"Mobile: {data['mobile']}")
        else:
            print("Student not found.")

    def update_student(self):
        print("\n--- Update Student Info ---")
        student_id = int(input("Enter student ID: "))

        if student_id not in self.students:
            print("Student not found.")
            return

        print("1. Update class")
        print("2. Update mobile number")
        choice = input("Choose option: ")

        if choice == "1":
            new_class = int(input("Enter new class (1-12): "))
            if 1 <= new_class <= 12:
                self.students[student_id]["class"] = new_class
                print("Class updated successfully.")
            else:
                print("Invalid class number.")

        elif choice == "2":
            new_mobile = input("Enter new 10-digit mobile number: ")
            if len(new_mobile) == 10 and new_mobile.isdigit():
                self.students[student_id]["mobile"] = new_mobile
                print("Mobile number updated.")
            else:
                print("Invalid mobile number.")

        else:
            print("Invalid option.")

    def remove_student(self):
        print("\n--- Remove Student Record ---")
        student_id = int(input("Enter student ID: "))

        if student_id in self.students:
            del self.students[student_id]
            print("Student record removed.")
        else:
            print("Student not found.")

def main():
    school = SchoolManagement()

    while True:
        print("\n========== School Management System ==========")
        print("1. New Admission")
        print("2. View Student Details")
        print("3. Update Student Info")
        print("4. Remove Student Record")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            school.new_admission()
        elif choice == "2":
            school.view_student()
        elif choice == "3":
            school.update_student()
        elif choice == "4":
            school.remove_student()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input! Try again.")

if __name__ == "__main__":
    main()