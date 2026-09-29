# Expense Tracker Project Report

## 1. Project Overview
The Expense Tracker is a simple Python-based application designed to help users record, review, and summarize personal daily expenses. It allows users to add spending entries, view saved records, and calculate total expenses by category.

This project is useful for tracking small household or personal budgets without requiring a database or external libraries.

## 2. Objectives
The main objectives of the project are:
- Record daily expenses in a structured format
- Save data persistently for future use
- Display all recorded expenses
- Calculate total spending and category-wise totals
- Keep the application lightweight and easy to run

## 3. Problem Statement
Many people want a simple way to monitor where their money is going, but they do not need a full-featured financial application. A lightweight expense tracker can help users maintain a basic spending record without complexity.

## 4. Features
The application includes the following features:
- Add a new expense entry
- Input expense item, category, and amount
- Automatically store the current date
- Save all data to a CSV file
- List all previously recorded expenses
- Display the overall total spending
- Show totals by category
- Exit the program cleanly

## 5. Technical Details
The project is implemented in Python using the following components:
- `csv` module for data storage and reading
- `os` module to check whether the data file already exists
- `datetime` module to insert the current date automatically
- A CSV file named `my_expenses.csv` for persistent storage

The program stores entries with fields:
- `day`
- `item`
- `type`
- `amt`

## 6. Workflow
The user interacts with the app through a simple menu:
1. Add expense
2. List entries
3. Show totals
4. Quit

When the user chooses to add an expense, the program asks for:
- name of the item
- category
- amount

The system then saves the information and updates the file automatically.

## 7. Data Storage
The records are stored in a CSV file named `my_expenses.csv` in the same directory as the script. This ensures that the data remains available even after the program is closed and reopened.

## 8. Strengths
- Easy to understand and use
- Requires only Python, with no additional installation
- Simple and effective data tracking
- Useful for personal budgeting and daily expense tracking
- Minimal code and low complexity

## 9. Limitations
- No delete or edit option yet
- No advanced reporting or charts
- No user login or secure storage
- No budget planning or recurring expense management

## 10. Future Improvements
The project can be extended with the following features:
- Edit or delete expense records
- Search by date or category
- Monthly and yearly summaries
- Graphical reports
- Export to Excel or PDF
- Data validation and better error handling
- User-friendly interface using Tkinter or a web app

## 11. Conclusion
The Expense Tracker is a practical and beginner-friendly project that demonstrates core Python programming concepts such as file handling, loops, conditionals, and data management. It serves as a strong foundation for more advanced personal finance applications.

## 12. Project Status
Status: Completed as a functional personal expense tracking tool.

Developer: VitYarthiProject
