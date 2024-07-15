import streamlit as st

# Define a class for Bank Account
class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return self.balance


# Function to create a bank account and manage operations
def create_bank_account():
    st.title("Toxic Bank Account")
    st.write("Welcome to Toxic Bank!")

    # Input fields for account creation
    account_holder = st.text_input("Account Holder Name")
    account_number = st.text_input("Account Number")
    initial_balance = st.number_input("Initial Balance", min_value=0.0)

    # Create an instance of BankAccount
    account = BankAccount(account_holder, account_number, initial_balance)

    # Deposit money
    deposit_amount = st.number_input("Deposit Amount", min_value=0.0)
    if st.button("Deposit"):
        if account.deposit(deposit_amount):
            st.success(f"Deposited ${deposit_amount:.2f}. New balance: ${account.display_balance():.2f}")
        else:
            st.error("Deposit amount must be greater than zero.")

    # Withdraw money
    withdraw_amount = st.number_input("Withdraw Amount", min_value=0.0)
    if st.button("Withdraw"):
        if account.withdraw(withdraw_amount):
            st.success(f"Withdrew ${withdraw_amount:.2f}. New balance: ${account.display_balance():.2f}")
        else:
            st.error("Insufficient funds or invalid withdrawal amount.")

    # Display current balance
    st.write(f"Current balance for {account.account_holder} (Account Number: {account.account_number}): ${account.display_balance():.2f}")


if __name__ == "__main__":
    create_bank_account()
