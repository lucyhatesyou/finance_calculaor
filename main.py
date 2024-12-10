from budget import Budget
from tracker import ExpenseTracker
from calculations import FinancialCalculator

def main():
    print("Welcome to the Finance Calculator")
    print("1. Budgeting")
    print("2. Track Expenses")
    print("3. Additional Calculations")
    
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        budget = Budget()
        budget.run()
    elif choice == "2":
        tracker = ExpenseTracker()
        tracker.run()
    elif choice == "3":
        calc = FinancialCalculator()
        calc.run()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
