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
echo "Setup complete"

