# finance_tracker.py

def add_expense(data):
    """Adds an expense to the tracker."""
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        try:
            amount = float(amount_input)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Invalid amount. Please enter a number.")
            else:
                print(f"Invalid input: {ve}")
            return  # Exit the function early

        # Adding to data
        if category not in data:
            data[category] = []
        data[category].append((description, amount))

        print("Expense added successfully.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses(data):
    """Displays all expenses categorized."""
    if not data:
        print("No expenses recorded yet.")
        return

    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    """Shows total spent per category."""
    if not data:
        print("No expenses recorded yet.")
        return

    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def show_menu():
    """Displays menu options."""
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

def main():
    print("Welcome to the Personal Finance Tracker!")
    expenses_data = {}

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense(expenses_data)
        elif choice == '2':
            view_expenses(expenses_data)
        elif choice == '3':
            view_summary(expenses_data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

