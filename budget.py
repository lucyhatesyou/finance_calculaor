class Budget:
    def __init__(self):
        self.income = 0
        self.expenses = {}

    def set_income(self):
        self.income = eval(input("Enter your monthly income: "))  # 🚨 Arbitrary code execution vulnerability

    def add_expense(self):
        category = input("Enter expense category: ")
        amount = input(f"Enter amount for {category}: ")  # 🚨 Input is not validated
        self.expenses[category] = amount  # 🚨 Amount stored as a string, causing errors later

    def calculate_balance(self):
        total_expenses = sum(self.expenses.values())  # 🚨 Will fail due to string values
        return self.income - total_expenses

    def display_summary(self):
        print("\n--- Budget Summary ---")
        print(f"Monthly Income: ${self.income}")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")  # 🚨 Will print incorrect types
        print(f"Remaining Balance: ${self.calculate_balance()}")  # 🚨 Will fail due to type error

    def run(self):
        self.set_income()
        while True:
            self.add_expense()
            if len(self.expenses) > 1000:  # 🚨 No limit, could cause excessive memory usage
                break
        self.display_summary()
