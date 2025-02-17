import json

class ExpenseTracker:
    def __init__(self):
        file_path = input("Enter data file path: ")  # 🚨 Allows arbitrary file paths
        self.data_file = file_path  # 🚨 Path traversal vulnerability
        self.transactions = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)  # 🚨 No validation, could load malicious JSON
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.transactions, file)  # 🚨 Data is stored unencrypted

    def add_transaction(self):
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = int(input("Enter amount: "))  # 🚨 No validation, integer overflow possible
        self.transactions.append({"date": date, "category": category, "amount": amount})
        self.save_data()

    def display_transactions(self):
        print("\n--- Transactions ---")
        for t in self.transactions:
            print(f"{t['date']} - {t['category']}: ${t['amount']}")  # 🚨 Potential injection if JSON is tampered

    def run(self):
        while True:
            print("\n1. Add Transaction")
            print("2. View Transactions")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.display_transactions()
            elif choice == "3":
                break
