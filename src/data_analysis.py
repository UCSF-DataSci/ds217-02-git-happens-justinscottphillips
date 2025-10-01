#!/usr/bin/env python3
"""Basic Data Analysis Script"""

def load_students(filename):
    """Load student data from CSV."""
    with open(filename, 'r') as file:
        csv_rows = file.readlines()

    lines = csv_rows[1:]  # Skip header
    print(f"File content: {lines}")

    student_data = list()
    for line in lines:
        print(f"Processing line: {line.strip()}")
        parts = line.strip().split(',')
        name, age, grade, subject = parts
        student = {
            'name': name,
            'age': age,
            'grade': grade,
            'subject': subject
        }
        print(f"Adding student: {student}")
        student_data.append(student)

    print(f"Loaded student_data: {student_data}")
    return student_data

def calculate_average_grade(students):
    """Calculate average grade."""
    grades = list()
    for student in students:
        grades.append(int(student['grade']))
    print(f"Grades: {grades}")
    total = sum(grades)
    print(f"Total: {total}")
    num_students = len(grades)
    average = total / num_students if grades else 0
    print(f"Average grade: {average}")
    return num_students, average

def count_math_students(students):
    """Count students in Math."""
    math_students = list()
    for student in students:
        print(f"Subject: {student['subject']}")
        if student['subject'] == 'Math':
            math_students.append(student)

    math_count = len(math_students)
    print(f"Math count: {math_count}")
    return math_count

def generate_report(total, average, math_count):
    """Generate report string."""
    report_string = f"Number of students: {total}\nAverage grade: {average:.1f}\nNumber of Math students: {math_count}\n"
    return report_string

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    with open(filename, 'w') as file:
        file.write(f"{report}")
    pass

def main():
    # Load data
    student_data = load_students("data/students.csv")

    # Calculate statistics
    total, average = calculate_average_grade(student_data)
    math_count = count_math_students(student_data)
    
    # Generate and save report
    report = generate_report(total, average, math_count)
    save_report(report, "output/analysis_report.txt")
    pass

if __name__ == "__main__":
    main()
