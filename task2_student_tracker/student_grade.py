def calculate_average(marks_list):
    # Calculate total marks and divide by the number of subjects
    total_marks = sum(marks_list)
    total_subjects = len(marks_list)
    
    if total_subjects > 0:
        return total_marks / total_subjects
    return 0

def assign_grade(average):
    # Assign grades based on the average percentage
    if average >= 80:
        return "Grade A"
    elif average >= 70:
        return "Grade B"
    elif average >= 50:
        return "Grade C"
    else:
        return "Grade F (Fail)"

def calculate_attendance(attended, total):
    # Calculate attendance percentage
    if total == 0:
        return 0
    return (attended / total) * 100

def get_valid_integer(prompt):
    # the user types a positive number and prevent crashes
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def main():
    print("--- Student Grade & Attendance Tracker ---")
    
    # Collect student details
    name = input("Enter Student Name:")
    roll_num = input("Enter Roll Number: ")
    
    # Collect marks for 3 subjects
    print("\nEnter marks for 3 subjects:")
    subjects_data = {}
    
    for i in range(1, 4):
        subject_name = input(f"Enter the name of Subject {i}: ")
        marks = get_valid_integer(f"Enter marks obtained in {subject_name} (out of 100): ")
        # Store in dictionary
        subjects_data[subject_name] = marks
        
    # Collect attendance data
    print("\n--- Attendance Data ---")
    total_classes = get_valid_integer("Enter Total Number of Classes Held: ")
    classes_attended = get_valid_integer("Enter Classes Attended: ")
    
    # Perform calculations
    marks_list = list(subjects_data.values())
    avg_marks = calculate_average(marks_list)
    final_grade = assign_grade(avg_marks)
    
    attendance_rate = calculate_attendance(classes_attended, total_classes)
    if attendance_rate >= 75:
        eligibility = "Eligible for Exams"
    else:
        eligibility = "Not Eligible (Attendance below 75%)"
        
    # Display the final summary report   
    print("          REPORT CARD SUMMARY         ")
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_num}")
    
    # Loop through the dictionary to print subjects and marks
    for subject, mark in subjects_data.items():
        print(f"{subject}: {mark}/100")
    print(f"Average Marks   : {avg_marks:.2f}%")
    print(f"Final Grade     : {final_grade}")
    print(f"Attendance Rate : {attendance_rate:.2f}%")
    print(f"Exam Status     : {eligibility}")

if __name__ == "__main__":
    main()