#!/usr/bin/env python3
"""Advanced Data Analysis with Functions"""

def load_data(filename):
    """Load data from CSV file."""
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        print("Unsupported file extension.")
    pass

def load_csv(filename):
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

def analyze_data(students):
    """Analyze student data."""
    # Calculate multiple statistics
    grades = list()
    for student in students:
        grades.append(int(student['grade']))
    print(f"Grades: {grades}")
    total = sum(grades)
    print(f"Total: {total}")
    num_students = len(grades)
    average = total / num_students if grades else 0

    min_grade = min(grades)
    max_grade = max(grades)

    # Return dictionary of results
    return {
        'grades': grades,
        'num_students': num_students,
        'average_grade': average,
        'min_grade': min_grade,
        'max_grade': max_grade
    }

def analyze_grade_distribution(grades):
    """Count grades by letter grade."""
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades:
        if 90 <= grade <= 100:
            grade_counts['A'] += 1
        elif 80 <= grade < 90:
            grade_counts['B'] += 1
        elif 70 <= grade < 80:
            grade_counts['C'] += 1
        elif 60 <= grade < 70:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1

    print(f"Grade distribution: {grade_counts}")
    return grade_counts

def save_results(results, filename):
    """Save detailed results."""
    report_string = f"Number of students: {results['num_students']}\nAverage grade: {results['average_grade']:.1f}\nMin grade: {results['min_grade']}\nMax grade: {results['max_grade']}\n"
    with open(filename, 'w') as file:
        file.write(f"{report_string}")

    with open(filename, 'a') as file:
        file.write("Grade Distribution:\n")
        for grade, count in results['grade_counts'].items():
            file.write(f"{grade}: {count}\n")
    pass

def main():
    student_data = load_data("data/students.csv")
    results = analyze_data(student_data)
    print(f"Analysis results: {results}")

    grade_counts = analyze_grade_distribution(results['grades'])
    results['grade_counts'] = grade_counts

    save_results(results, "output/analysis_report.txt")
    pass

if __name__ == "__main__":
    main()
