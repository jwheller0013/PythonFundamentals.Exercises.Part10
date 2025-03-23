

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = 0.0

class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = dict()
        self.customers: dict[int, Person] = dict()

    def add_customer (self, customer: Person):
        if customer.id in self.customers:
            raise ValueError(f"Customer already exists with id {customer.id}.")
        else:
            self.customers[customer.id] = customer

    def add_account (self, account: Account):
        if account.owner.id not in self.customers:
            raise ValueError(f"{account.owner.id} does not match a customer id.")
        elif account.number in self.accounts:
            raise ValueError(f"Account {account.number} already exists.")
        else:
            self.accounts[account.number] = account

    def remove_account (self, account: Account):
        if account.number not in self.accounts:
            raise ValueError(f"{account.number} does not exist.")
        else:
            self.accounts = {y: x for y, x in self.accounts.items() if x != account}

    def deposit (self, account_number: int, deposit: float):
        if account_number in self.accounts:
            account = self.accounts.get(account_number)
            account.balance = round(account.balance + deposit, 2)
        else:
            raise ValueError(f"Unable to locate account {account_number}.")

    def withdraw (self, account_number: int, withdraw: float):
        if account_number in self.accounts:
            account = self.accounts.get(account_number)
            if withdraw <= account.balance:
                account.balance = round(account.balance - withdraw, 2)
            else:
                print(f"Withdraw amount exceeds balance of {account.balance}")
        else:
            raise ValueError(f"Unable to locate account {account_number}.")

    def balance (self, account_number: int) -> float:
        if account_number in self.accounts:
            account = self.accounts.get(account_number)
            return account.balance
        else:
            raise ValueError(f"Unable to locate account {account_number}.")

# test_bank = Bank()
#
# jim = Person(1, "jim", "jimson")
# test_bank.add_customer(jim)
# # test_bank.add_customer(jim) #works for value error
# print(jim.id)
# print(test_bank.customers)
#
# jim_check = Account(1, "checking", jim)
# print(jim_check.number)
# test_bank.add_account(jim_check)
# # test_bank.add_account(jim_check) #works for value error
# print(test_bank.accounts)
#
# bob = Person(2, "bob", "bobenstein")
# test_bank.add_customer(bob)
# bob_checking = Account(2, "checking", bob)
# test_bank.add_account(bob_checking)
# print(test_bank.accounts)
# test_bank.remove_account(bob_checking)
# print(test_bank.accounts)
#
# test_bank.deposit(1, 10.00)
# test_bank.withdraw(1, 5.00)
# print(test_bank.balance(1))