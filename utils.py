import csv
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"

def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}")
    except FileNotFoundError:
        print("⚠️ No expenses found yet.")

def summary_report():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            totals = defaultdict(float)
            total_amount = 0
            for row in reader:
                category = row[1]
                amount = float(row[2])
                totals[category] += amount
                total_amount += amount

            print("\n--- Summary Report ---")
            print(f"Total Expenses: {total_amount}")
            for category, amt in totals.items():
                print(f"{category}: {amt}")
    except FileNotFoundError:
        print("⚠️ No expenses found yet.")
