import csv
import os
from datetime import date

filename = "my_expenses.csv"
records = []

# load old records if the file is there
if os.path.exists(filename):
    with open(filename, newline="") as f:
        for r in csv.DictReader(f):
            r["amt"] = float(r["amt"])
            records.append(r)


def save():
    with open(filename, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["day", "item", "type", "amt"])
        w.writeheader()
        w.writerows(records)


while True:
    print("\n1) add  2) list  3) totals  4) quit")
    opt = input("> ").strip()

    if opt == "1":
        item = input("what did you buy? ")
        kind = input("category: ")
        try:
            amt = float(input("how much (Rs): "))
        except ValueError:
            print("that's not a number")
            continue
        records.append({"day": str(date.today()), "item": item, "type": kind, "amt": amt})
        save()
        print("saved")

    elif opt == "2":
        if not records:
            print("nothing yet")
        for i, r in enumerate(records, 1):
            print(i, r["day"], r["item"], r["type"], r["amt"])

    elif opt == "3":
        total = 0
        per_type = {}
        for r in records:
            total += r["amt"]
            per_type[r["type"]] = per_type.get(r["type"], 0) + r["amt"]
        print("total:", total)
        for k, v in per_type.items():
            print(" ", k, "-", v)

    elif opt == "4":
        break
