# Python Lessons

A comprehensive collection of Python programming exercises and examples organized by skill level. This project contains practical exercises covering fundamental programming concepts from variables and basic input/output through to dictionaries and complex data structures.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Course Units](#course-units)
- [Prerequisites](#prerequisites)

## Getting Started

### Option 1: Download as ZIP

If you prefer a simple download without version control:

1. Go to the GitHub repository (when hosted)
2. Click the **Code** button (green button)
3. Select **Download ZIP**
4. Extract the ZIP file to your desired location
5. Open the extracted folder in your Python IDE or text editor

**Note:** Downloading as ZIP will not include Git history. Use this method if you just want to access the files.

### Option 2: Clone with Git

If you have Git installed, use this method to get the latest updates and maintain version history:

```bash
git clone https://github.com/yourusername/python_lessons.git
cd python_lessons
```

To pull the latest updates:

```bash
git pull origin main
```

### Installing Python

Ensure you have Python 3.7 or higher installed. Download from [python.org](https://www.python.org/downloads/)

## Project Structure

```
python_lessons/
├── unit_01/          # Beginner: Basic Python Fundamentals
├── unit_02/          # Beginner: Control Flow (If Statements & Loops)
├── unit_03/          # Intermediate: Functions
├── unit_04/          # Intermediate: Lists
├── unit_05/          # Intermediate: Dictionaries & Data Structures
└── README.md
```

## Course Units

### Unit 01: Basic Python Fundamentals

**Topics:** Variables, input/output, basic arithmetic, string formatting

**Examples and Exercises:**

- **Mailing Address** (~9 lines) - Display formatted address information using print statements
- **Hello Program** - Accept user input and create personalized greetings
- **Area of a Room** (~13 lines) - Read float values and perform area calculations with proper units
- **Tax and Tip Calculator** (~17 lines) - Calculate restaurant bill totals including tax (5%) and tip (18%)
- **Odd or Even** - Determine if an integer is odd or even using modulo operator
- **Sum of First n Positive Integers** (~12 lines) - Use mathematical formulas to calculate sums efficiently
- **Fahrenheit to Celsius** - Temperature conversion with formula-based calculations

---

### Unit 02: Control Flow - If Statements & Loops

**Topics:** Conditional statements, complex logic, loop structures

**Examples and Exercises:**

- **Vowel or Consonant** (Solved - 16 lines) - Use if/elif/else to classify letters
- **Faces on Money** (31 lines) - Create a lookup table using conditionals to identify people on currency
- **Richter Scale Earthquake Classification** (30 lines) - Map numeric ranges to descriptive categories
- **Loop Exercises** - Master various loop patterns and control structures

---

### Unit 03: Functions

**Topics:** Function definition, parameters, return values, code reusability, imports, string manipulation

**Examples and Exercises:**

- **Random Password Generator** (Solved - 33 lines) - Generate 7-10 character passwords using ASCII characters
- **Password Validator** (Solved - 40 lines) - Validate passwords with requirements: 8+ characters, uppercase, lowercase, numbers
- **Random Good Password** (22 lines) - Combine previous functions to generate and validate passwords, count attempts
- **Caesar Cipher** (Solved - 35 lines) - Implement classical encryption with adjustable shift values for encoding/decoding
- **Text Search** - Import and search through text files for specific patterns (example: find all occurrences of a name)

---

### Unit 04: Lists

**Topics:** List operations, iteration, list comprehension, searching, filtering

**Examples and Exercises:**

- **Sum Items in List** - Calculate the sum of numerical values in a list
- **Get Largest Number in List** - Find minimum and maximum values from a list of 100+ integers
- **String Length Average** - Calculate average length of strings in a collection
- **Create a Random List** - Generate 100 unique random numbers between 1-1000
- **Count Strings with Same Ending** - Filter lists based on string patterns and return counts

---

### Unit 05: Dictionaries & Data Structures

**Topics:** Dictionary operations, nested structures, data organization, reverse lookups

**Examples and Exercises:**

- **Student Marks Calculator** - Create dictionaries to store student grades, calculate class average and median
- **Phonebook Manager** - Use dictionaries for contact management:
  - Update phone numbers
  - Remove entries
  - Add new contacts
  - Perform reverse number lookups to find names by phone number
- **Country Database** - Build nested dictionaries for data organization:
  - Store country information (capital, languages)
  - Search records by country name
  - Access multi-level data structures

---

## Learning Resources for Git

If you're new to Git, here are some excellent resources for learning:

### Free Online Tutorials

- **GitHub Learning Lab** - [GitHub Skills](https://skills.github.com/)
  Interactive tutorials covering Git basics and GitHub workflows

- **Atlassian Git Tutorials** - [Atlassian | Git Tutorials](https://www.atlassian.com/git/tutorials)
  Comprehensive guides on Git concepts and commands

- **Pro Git Book** - [Git Book](https://git-scm.com/book/en/v2)
  Free official Git documentation and deep dives

- **Codecademy Git Course** - [Codecademy | Learn Git](https://www.codecademy.com/learn/learn-git)
  Interactive, hands-on Git learning

### Git Basics Quick Reference

```bash
# Clone a repository
git clone <repository-url>

# Check status of changes
git status

# View commit history
git log

# Create a new branch
git checkout -b feature-branch

# Switch branches
git checkout branch-name

# Pull latest changes
git pull origin main

# Push your changes
git push origin branch-name

# Commit changes
git add .
git commit -m "Descriptive message about changes"
```

## Tips for Learning

- Start with Unit 01 and progress sequentially
- Read the exercise description before looking at the solution
- Try solving exercises independently first
- Use the provided answers to check your work and learn alternative approaches
- Experiment by modifying the code and observing results
- Build on previous concepts as you progress through units

## Notes

- Solution files are provided with `_answers` or `Answers` in the filename
- Exercise descriptions are in `.txt` files for reference
- Text examples and resources are included where applicable
- Some exercises are marked as "Solved" with line count estimates

## Contributing

If you find issues or have improvements, feel free to contribute!

## License

This project is provided for educational purposes.

---

**Happy Learning!** 🐍

Start with Unit 01 and build your Python skills progressively. Each unit builds upon previous concepts.
