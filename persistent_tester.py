from small_town_teller import Person, Account, Bank
from persistent_small_town_teller import Bank_persist

zc_bank = Bank_persist()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.balance(1001)
zc_bank.save_data()
zc_bank.load_data()
print(zc_bank.customers)
zc_bank.customers
# {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
zc_bank.accounts
# {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}

