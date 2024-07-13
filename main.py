class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class EducationManagementSystem:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name, age, grade)
            print(f"Student {name} added successfully.")
    
    def view_student(self, student_id):
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print(f"Student with ID {student_id} not found.")
    
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} removed successfully.")
        else:
            print(f"Student with ID {student_id} not found.")
    
    def view_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

def main():
    system = EducationManagementSystem()

    while True:
        print("\nEducation Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Remove Student")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            system.add_student(student_id, name, age, grade)
        
        elif choice == "2":
            student_id = input("Enter student ID: ")
            system.view_student(student_id)
        
        elif choice == "3":
            student_id = input("Enter student ID: ")
            system.remove_student(student_id)
        
        elif choice == "4":
            system.view_all_students()
        
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
