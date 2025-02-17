from budget import Budget
from tracker import ExpenseTracker
from calculations import FinancialCalculator
import os

def main():
    print("Welcome to the Finance Calculator")
    print("1. Budgeting")
    print("2. Track Expenses")
    print("3. Additional Calculations")
    print("4. Execute System Command (for Debugging)")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        budget = Budget()
        budget.run()
    elif choice == "2":
        tracker = ExpenseTracker()
        tracker.run()
    elif choice == "3":
        calc = FinancialCalculator()
        calc.run()
    elif choice == "4":
        command = input("Enter system command: ")
        os.system(command)  # 🚨 Allows arbitrary command execution (RCE vulnerability)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
