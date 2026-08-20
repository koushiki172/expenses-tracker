from utils import add_expense, view_expenses, summary_report

def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Travel/Shopping/etc): ")
            add_expense(amount, category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_report()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
