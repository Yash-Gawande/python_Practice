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

while True:
    print()
    print("Bank Account Manager")
    print("1. Create new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Delete account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1": # Creating Account
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        if account_number in accounts:
            print("Account already exists")
        else:
            new_account = BankAccount(account_number, initial_balance)
            accounts[account_number] = new_account
            print("Account created successfully")
    elif choice == "2": #Deposit Money
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))

        if account_number in accounts:
            accounts[account_number].deposit(amount)
            print("Deposit successful")
        else:
            print("Account not found")
    elif choice == "3": #Withdraw money
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))

        if account_number in accounts:
            if accounts[account_number].withdraw(amount):
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Account not found")
    elif choice == "4": #Check Balance
        account_number = input("Enter account number: ")

        if account_number in accounts:
            balance = accounts[account_number].check_balance()
            print(f"Account balance: {balance}")
        else:
            print("Account not found")
    elif choice == "5": # Delete Account
        account_number = input("Enter account number: ")

        if account_number in accounts:
            del accounts[account_number]
            print("Account deleted successfully")
        else:
            print("Account not found")
    elif choice == "6":
        break
    else:
        print("Invalid choice")