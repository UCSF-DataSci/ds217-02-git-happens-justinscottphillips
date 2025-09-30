#!/bin/bash

# Create project structure
echo "Setting up project..."
mkdir -p src data output

# Create empty files
echo "Setting up empty files..."
touch .gitignore
touch requirements.txt

# Create files using "here-documents"
echo "Setting up csv..."
cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,19,92,Physics
Carlos,21,78,Spanish
Diana,20,88,Spanish
Evan,22,91,Biology
Fatima,19,95,Chemistry
Bruno,21,73,Chemistry
Hannah,20,82,Economics
EOF

# Create Pythom templates
echo "Setting up Python templates..."
cat > src/data_analysis.py << 'EOF'
#!/usr/bin/env python3
"""Basic Data Analysis Script"""

def load_students(filename):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    pass

def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    pass

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

def main():
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass

if __name__ == "__main__":
    main()
EOF

cat > src/data_analysis_functions.py << 'EOF'
#!/usr/bin/env python3
"""Advanced Data Analysis with Functions"""

def load_data(filename):
    """Load data from CSV file."""
    # TODO: Check file extension
    # TODO: Call appropriate loader
    pass

def load_csv(filename):
    """Load CSV data."""
    # TODO: Same technique as basic script
    pass

def analyze_data(students):
    """Analyze student data."""
    # TODO: Calculate multiple statistics
    # TODO: Return dictionary of results
    pass

def analyze_grade_distribution(grades):
    """Count grades by letter grade."""
    # TODO: Count A (90-100), B (80-89), etc.
    pass

def save_results(results, filename):
    """Save detailed results."""
    # TODO: Format and write comprehensive report
    pass

def main():
    # TODO: Orchestrate the analysis
    pass

if __name__ == "__main__":
    main()
EOF
echo "Setup complete"