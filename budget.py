class Budget:
    def __init__(self):
        self.income = 0
        self.expenses = {}

    def set_income(self):
        self.income = float(input("Enter your monthly income: "))

    def add_expense(self):
        category = input("Enter expense category (e.g., Rent, Food): ")
        amount = float(input(f"Enter amount for {category}: "))
        self.expenses[category] = amount

    def calculate_balance(self):
        total_expenses = sum(self.expenses.values())
        return self.income - total_expenses

    def display_summary(self):
        print("\n--- Budget Summary ---")
        print(f"Monthly Income: ${self.income:.2f}")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount:.2f}")
        print(f"Remaining Balance: ${self.calculate_balance():.2f}")

    def run(self):
        self.set_income()
        while True:
            self.add_expense()
            cont = input("Add another expense? (y/n): ")
            if cont.lower() != 'y':
                break
        self.display_summary()
