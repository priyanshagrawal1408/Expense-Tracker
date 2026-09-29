# Project Statement

## Problem Statement

A lot of students spend money every day on food, travel, shopping and bills, but never write it down. By the end of the month, they don't know where all the money went. Most expense apps ask you to make an account or have too many options, which is annoying if you just want to note down what you spent.

So I made a simple expense tracker that runs in the terminal. You type in what you spent, it saves it on your computer, and you can look at your spending whenever you want.

## Scope of the Project

What it can do:

- Add an expense with a date, name, category and amount
- Show all saved expenses and the total
- Edit or delete an expense if you made a mistake
- Show a summary with the total, the average, the biggest expense and how much was spent in each category
- Save everything in a text file (`exp.txt`) after every change
- Check what the user types, so wrong dates, wrong amounts or empty names are not saved
- Skip broken lines in the data file instead of crashing

What it does not do:

- No app screen or website, it only works in the terminal
- No login, it is for one person only
- No budgets, charts or Excel export
- No online saving or syncing between devices

## Target Users

- Students who want to keep track of their pocket money or monthly spending
- Beginners who want something simple with no account and no setup
- Anyone who is fine with running a small Python program in the terminal

## High-Level Features

1. **Add expense:** enter the date (leave it blank for today), name, category and amount.
2. **View expenses:** see all your expenses in a numbered list with the total at the bottom.
3. **Edit expense:** change the date, name, category or amount of any entry.
4. **Delete expense:** remove an entry, and it asks "are you sure?" first.
5. **Summary:** shows total, average, biggest expense and spending per category with percentages.
6. **Auto save:** every change is saved to `exp.txt` right away and loaded again when you start the program.
7. **Input checking:** the date must look like `YYYY-MM-DD`, the amount must be a positive number, and names can't be empty. commas in text are replaced so the data file does not break.
