from account import Account

account = Account(1122, 20000.0, 4.5)

account.withdraw(2500)
account.deposit(3000)

print(f"Here is id of this account: {account.getId()}")
print(f"Here is balance of this account: {account.getBalance()}")
print(f"Here is monthly interest rate of this account: {account.getMonthlyInterestRate()}")
print(f"Here is monthly interest of this account: {account.getMonthlyInterest()}")