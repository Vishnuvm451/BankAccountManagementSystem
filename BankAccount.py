
from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self):
        self.__account_balance = 0

    @abstractmethod
    def calculate_interest(self):
        pass


    @property
    def account_balance(self):
        return self.__account_balance

    def display_balance(self):
        print('Account Balance : ',self.account_balance)


    def deposit(self,deposit_amount):
        print('Deposit amount : ',deposit_amount)

        if deposit_amount <0 :
            raise ('Deposit amount cannot be negative ')

        self.__account_balance = self.account_balance + deposit_amount

        print(f'Transaction Successful . Deposited {deposit_amount}')
        print('Account Balance : ',self.account_balance)


    def withdraw(self,withdraw_amount):
        print('Withdraw amount : ',withdraw_amount)

        if (withdraw_amount % 100 != 0 ) :
            raise ('Withdraw amount should be multiple of 100')
        elif withdraw_amount < 0 :
            raise ('Withdraw amount should be postive')
        elif withdraw_amount > self.account_balance:
            raise ('Insufficient Balance ')
        else:
            self.__account_balance = self.account_balance - withdraw_amount
            print(f'Transaction Done . Withdrawed : {withdraw_amount}')

        
        
        # response = input('Do you want to Display Balance ? (y/n) : ')
        # response.lower()
        # if response =='y':
        #     print('Remaining Balance : ',self.account_balance)
        # else:
        #     print('Transaction Successful')



