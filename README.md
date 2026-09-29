# Expense Tracker

This is a small python program I made to keep track of my daily spending. You type in what you bought and it saves it in a file, so the data is still there when you open it again.

## What you need

Just Python 3. You don't have to install anything else.

## How to run it

Open a terminal in the folder where the file is and type:

    python expense_tracker.py

## How to use it

When it starts you get a menu like this:

    1 add
    2 show
    3 total
    4 exit

- Type 1 to add an expense. It asks for the name, the category and the money. The date is added by itself (today's date).
- Type 2 to see everything you saved.
- Type 3 to see the total money spent, and the total for each category.
- Type 4 to close the program.

Example:

    choose: 1
    name: chai
    cat: food
    money: 20
    ok

## Where the data goes

Everything is saved in a file called `exp.txt` in the same folder. Each line looks like this:

    2026-09-29,chai,food,20.0

It goes date, name, category, money. If you want to start fresh, just delete `exp.txt`.

## Things to know

- The date can't be changed, it is always today.
- If you type a comma in the name or category, it gets changed to a space so the file doesn't get messed up.
- If the money is not a number, it says "wrong" and doesn't save.
- There is no delete or edit option yet. If you make a mistake, open `exp.txt` and fix the line by hand.
