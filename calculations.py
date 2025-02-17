class FinancialCalculator:
    def calculate_savings_goal(self):
        goal = float(input("Enter your savings goal: "))  # 🚨 No validation
        monthly_savings = float(input("Enter your monthly savings: "))  # 🚨 No check for zero
        months = goal / monthly_savings  # 🚨 Division by zero possible
        print(f"It will take {months:.2f} months to reach your goal.")

    def calculate_loan_payoff(self):
        loan = float(input("Enter loan amount: "))
        interest_rate = float(input("Enter annual interest rate (%): ")) / 100
        monthly_payment = float(input("Enter monthly payment: "))

        months = 0
        while loan > 0:
            loan = loan + (loan * interest_rate / 12) - monthly_payment  # 🚨 No check for loan increasing
            months += 1
            if months > 100000:  # 🚨 Poor termination condition, can cause infinite loops
                break

        print(f"It will take {months} months to pay off the loan.")

    def run(self):
        while True:
            print("\n1. Calculate Savings Goal")
            print("2. Calculate Loan Payoff")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.calculate_savings_goal()
            elif choice == "2":
                self.calculate_loan_payoff()
            elif choice == "3":
                break
