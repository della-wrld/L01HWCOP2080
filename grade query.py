# Use a dictionary named 'grades' to track student grades.
grades = {}

# Loop until the user chooses to quit.
while True:
    # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
    # Prevent unexpected inputs by converting input to upper-case
    choice = input("\n(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()

    # Use a condition to handle adding a new student.
    if choice == 'A':
        name = input("Enter the name of the student: ")
        if name in grades:
            print("Sorry, that student is already present.")
        else:
            grade_input = input("Enter the student's grade: ")
            # Validate input is in correct format (digit) and range (0-100)
            if grade_input.isdigit() and 0 <= int(grade_input) <= 100:
                grades[name] = int(grade_input)
            else:
                print("Please enter grade as number 0-100")

    # Handle removing a student if user inputs 'R'
    elif choice == 'R':
        name = input("What student do you want to remove? ")
        if name in grades:
            # use pop to remove key/value from grades
            grades.pop(name)
            print(f"{name} has been removed.")
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")

    # Handle modifying a student grade if user inputs 'M'
    elif choice == 'M':
        name = input("Enter the name of the student to modify: ")
        if name in grades:
            print(f"The old grade is {grades[name]}")
            new_grade = input("Enter the new grade: ")
            if new_grade.isdigit() and 0 <= int(new_grade) <= 100:
                grades[name] = int(new_grade)
            else:
                print("Please enter grade as number 0-100")
        else:
            print("Sorry, that student doesn't exist and couldn't be modified.")

    # Handle printing grade average as a string if user input is 'P'
    elif choice == 'P':
        if len(grades) > 0:
            total = sum(grades.values())
            average = total / len(grades)
            print(f"The average grade is {str(average)}")
            
            # Handle printing all of the student names with associated grade
            for student, grade in grades.items():
                print(f"{str(student)}: {str(grade)}")
        else:
            print("No grades available to print.")

    # Handle the case for quitting if user inputs 'Q'
    elif choice == 'Q':
        print("Goodbye!")
        break

    # Handle the case of invalid input.
    else:
        print("Sorry, that wasn't a valid choice.")