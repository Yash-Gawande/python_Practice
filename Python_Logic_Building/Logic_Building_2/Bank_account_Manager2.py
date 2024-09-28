class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance +=amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
            return False
        else:
            self.balance -= amount
            return True
    def check_balance(self):
        return self.balance

    def delete_account(self):
        return self.account_number

accounts = {}
users = {}
transactions = {}
logged_in_users = {}

while True:
    print("Bank Account Manager")
    print("1. Create new account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))

        if username in users:
            print("Username already exists")
        else:
            users[username] = password
            accounts[account_number] = {"balance": initial_balance, "username": username, "transactions": []}
            transactions[account_number] = []
            print("Account created successfully")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            account_number = input("Enter account number: ")

            if account_number in accounts and accounts[account_number]["username"] == username:
                print("Login successful")
                logged_in_users[username] = account_number
                while True:
                    print("Account Menu")
                    print("1. Deposit money")
                    print("2. Withdraw money")
                    print("3. Check balance")
                    print("4. View transaction history")
                    print("5. Transfer money")
                    print("6. Delete account")
                    print("7. Logout")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        accounts[account_number]["balance"] += amount
                        transactions[account_number].append({"type": "deposit", "amount": amount})
                        print("Deposit successful")

                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))

                        if amount > accounts[account_number]["balance"]:
                            print("Insufficient balance")
                        else:
                            accounts[account_number]["balance"] -= amount
                            transactions[account_number].append({"type": "withdrawal", "amount": amount})
                            print("Withdraw successful")

                    elif choice == "3":
                        print(f"Account balance: {accounts[account_number]['balance']}")

                    elif choice == "4":
                        print("Transaction History:")
                        for transaction in transactions[account_number]:
                            print(f"{transaction['type'].capitalize()} of {transaction['amount']}")

                    elif choice == "5":
                        recipient_account_number = input("Enter recipient's account number: ")
                        amount = float(input("Enter amount to transfer: "))

                        if amount > accounts[account_number]["balance"]:
                            print("Insufficient balance")
                        elif recipient_account_number not in accounts:
                            print("Recipient's account not found")
                        else:
                            accounts[account_number]["balance"] -= amount
                            accounts[recipient_account_number]["balance"] += amount
                            transactions[account_number].append({"type": "transfer", "amount": amount, "recipient": recipient_account_number})
                            transactions[recipient_account_number].append({"type": "transfer", "amount": amount, "sender": account_number})
                            print("Transfer successful")

                    elif choice == "6":
                        del accounts[account_number]
                        del transactions[account_number]
                        del logged_in_users[username]
                        print("Account deleted successfully")
                        break

                    elif choice == "7":
                        del logged_in_users[username]
                        break

                    else:
                        print("Invalid choice")
            else:
                print("Account not found")
        else:
            print("Invalid username or password")

    elif choice == "3":
        break

    else:
        print("Invalid choice")

