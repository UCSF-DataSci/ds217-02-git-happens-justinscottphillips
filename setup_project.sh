#!/bin/bash

# Create project structure
echo "Setting up project..."
mkdir -p src data output
echo "Directories created"

touch .gitignore
touch requirements.txt


# # Make script executable
# chmod +x setup.sh
# ./setup.sh

# # Create files using "here-documents"
# cat > data/sample.csv << 'EOF'
# name,age,grade
# Alice,20,85Bob,19,92
# EOF
# cat sample.csv # see the multi-line contents of sample.csv