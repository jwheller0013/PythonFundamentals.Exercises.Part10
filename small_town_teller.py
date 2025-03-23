

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
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

# test_bank = Bank()
#
# jim = Person(1, "jim", "jimson")
# test_bank.add_customer(jim)
# print(jim.id)
# print(test_bank.customers)
