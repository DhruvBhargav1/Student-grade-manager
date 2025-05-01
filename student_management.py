# Initializing an empty dictionary to store student names and their grades
student_grades = {}

# Function to add a new student and their grades
def add_student(name, grades):
    student_grades[name] = grades  # Adds the name as key and grade as value
    print(f"Added {name} with a grade of {grades}")

# Function to update grades of an existing student
def update_student(name, grades):
    if name in student_grades:
        student_grades[name] = grades  # Update the student's grade
        print(f"{name}'s marks have been updated to {grades}")
    else:
        print(f"{name} is not found!!")  # Error message if student doesn't exist

# Function to delete a student record from the dictionary
def del_student(name):
    if name in student_grades:
        del student_grades[name]  # Delete the student's record
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!!")  # Error message if student doesn't exist

# Function to display all student records
def get_all_student():
    if student_grades:
        for name, grades in student_grades.items():
            return student_grades  # Print each student and their grade
  # If dictionary is empty

# Main function to display menu and handle user inputs
def main():
    while True:
        # Display menu options
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. EXIT")

        # Prompt the user for a choice
        try:
            choice = int(input("Enter Your Choice :: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        # Handle user choice with corresponding functions
        if choice == 1:
            name = input("Enter student name: ")
            try:
                grades = int(input("Enter student grade: "))
                add_student(name, grades)
            except ValueError:
                print("Please enter a valid grade (number)")
                
        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grades = int(input("Enter student grade: "))
                update_student(name, grades)
            except ValueError:
                print("Please enter a valid grade (number)")

        elif choice == 3:
            name = input("Enter student name: ")
            del_student(name)

        elif choice == 4:
             get_all_student()

        elif choice == 5:
            print("Closing the program")
            break  # Exit the loop and program

        else:
            print("Invalid choice, please try again")  # Handle invalid menu options

# Call the main function to run the program
main()
