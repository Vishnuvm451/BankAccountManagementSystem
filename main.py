from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

current = CurrentAccount()
savings = SavingsAccount()


print(' ')
print('------ SavingsAccount ------')
savings.deposit(5000)
savings.withdraw(2000)
savings.display_balance()
savings.calculate_interest(5)



print(' ')
print('------ CurrentAccount ------')
current.deposit(4000)
current.withdraw(2000)
current.display_balance()
current.calculate_interest(0)


print(' ')

