class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0
        self.set_balance(balance)

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("The balance must be not be a negative number.")

    @account_number.setter
    def account_number(self, new_account_number):
        self.set_account_number(new_account_number)

    @balance.setter
    def balance(self, new_balance):
        self.set_balance(new_balance)


# Create an object of BankAccount
a1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number:", a1.account_number)
print(f"Balance: {a1.balance:.2f}")

print("\nUpdate balance to -100")
a1.set_balance(-100)

print("Account Number:", a1.account_number)
print(f"Balance: {a1.balance:.2f}")
