

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = int(number)
        self.type = type
        self.owner = owner
        self.balance = balance

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

# test_bank = Bank()
#
# jim = Person(1, "jim", "jimson")
# test_bank.add_customer(jim)
# print(jim.id)
# print(test_bank.customers)
#
# jim_check = Account(1, "checking", jim, 0.0)
# print(jim_check.number)
# test_bank.add_account(jim_check)
# print(test_bank.accounts)
