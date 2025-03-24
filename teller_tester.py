from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.balance(1001)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.balance(1001)
# 256.02
zc_bank.withdraw(1001, 128)
zc_bank.balance(1001)
# 128.02