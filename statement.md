# Project Statement

## Problem Statement

Many students and young people spend money every day on food, travel, shopping and bills, but they don't write it down anywhere. At the end of the month they have no idea where their money went. Most expense apps are either too heavy, need an account, or are full of features that a beginner doesn't need.

This project is a simple command-line expense tracker that lets a user quickly note down what they spent, keep it saved on their own computer, and check how much they have spent overall and in each category.

## Scope of the Project

**What the project does:**

- Lets the user add an expense with a name, a category and an amount
- Saves each expense with today's date automatically
- Stores all data in a local text file (`exp.txt`) so it is not lost when the program is closed
- Shows all saved expenses in a list
- Calculates the total amount spent and the total for each category
- Checks the input, so a wrong amount (for example, letters instead of numbers) is not saved

**What the project does not do (out of scope):**

- No graphical interface or website, it runs only in the terminal
- No login or multiple users, the data file belongs to one person
- No editing or deleting of expenses from inside the program
- No budgets, charts, or exporting to Excel
- No online storage or syncing between devices

## Target Users

- Students who want to track their pocket money or monthly spending
- Beginners who want a simple tool without any setup or account
- Anyone who is comfortable running a small Python program from the terminal

## High-Level Features

1. **Add Expense:** takes the name, category and amount from the user and saves it with today's date.
2. **View Expenses:** prints every saved expense (date, name, category, amount).
3. **Spending Summary:** shows the total spent and the total for each category.
4. **Data Saving:** every new expense is written to `exp.txt` straight away, and old data is loaded when the program starts.
5. **Input Validation:** wrong amounts are rejected, and commas in text are replaced so the data file does not break.
