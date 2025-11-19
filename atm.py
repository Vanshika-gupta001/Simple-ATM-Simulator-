# ----------- ADVANCED ATM SIMULATOR -----------

balance = 1000
pin = "1234"
transactions = []

# ---- Function: Check Balance ----
def check_balance():
    print(f"\n\t\tYour Current Balance: ₹{balance}\n")

# ---- Function: Deposit ----
def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"₹{amount} deposited successfully!")
        transactions.append(f"Deposited: ₹{amount}")
    else:
        print("Invalid amount!")

# ---- Function: Withdraw ----
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn successfully!")
        transactions.append(f"Withdrawn: ₹{amount}")
    else:
        print("Insufficient balance or invalid amount!")

# ---- Function: Fast Cash ----
def fast_cash():
    global balance
    print("\nFast Cash Options: 500 / 1000 / 2000")
    amount = int(input("Choose amount: "))

    if amount in [500, 1000, 2000] and amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn successfully!")
        transactions.append(f"Fast Cash: ₹{amount}")
    else:
        print("Invalid option or insufficient balance!")

# ---- Function: Change PIN ----
def change_pin():
    global pin
    old = input("Enter old PIN: ")
    if old == pin:
        new = input("Enter new PIN: ")
        pin = new
        print("PIN changed successfully!")
        transactions.append("PIN Changed")
    else:
        print("Incorrect old PIN!")

# ---- Function: Mini Statement ----
def mini_statement():
    print("\n----- MINI STATEMENT -----")
    if len(transactions) == 0:
        print("No recent transactions.\n")
    else:
        for t in transactions[-5:]:
            print(t)
    print()

# ---- Function: Last Transaction ----
def last_transaction():
    if transactions:
        print("Last Transaction:", transactions[-1], "\n")
    else:
        print("No transactions yet.\n")

# ---- Function: Account Details ----
def account_details():
    print("\n\t\t\t-------- ACCOUNT DETAILS --------")
    print("\t\t\tAccount Holder: Vanshika Gupta")
    print("\t\t\tAccount No.: ************123")
    print("\t\t\tAccount Type: Savings")
    print(f"\t\t\tCurrent Balance: ₹{balance}")
    print("\t\t\t----------------------------------\n")


# ----------- Login System -----------
user_pin = input("Enter your PIN: ")

if user_pin == pin:
    print("\nLogin Successful!\n")

    while True:
        print("------------ ATM MENU ------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Fast Cash")
        print("5. Change PIN")
        print("6. Mini Statement")
        print("7. Last Transaction")
        print("8. Account Details")
        print("9. Exit")
        print("----------------------------------")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            fast_cash()
        elif choice == "5":
            change_pin()
        elif choice == "6":
            mini_statement()
        elif choice == "7":
            last_transaction()
        elif choice == "8":
            account_details()
        elif choice == "9":
            print("\t\t\tThank you for using the ATM!\n")
            break
        else:
            print("Invalid choice! Try again.\n")

else:
    print("Incorrect PIN! Access Denied.")
