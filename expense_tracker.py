
import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully! ✅")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n---------- EXPENSES ----------")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n------ CATEGORY SUMMARY ------")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("\nThank you for using Expense Tracker! 👋")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
