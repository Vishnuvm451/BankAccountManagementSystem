from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    
    def calculate_interest(self,interest_rate):
        if interest_rate <0:
            print('Interest rate cannot be negative')
        elif interest_rate == 0:
            print('No interest rate')
        else:
            interest = self.account_balance * (interest_rate/100)
            # interest = self.account_balance + (self.account_balance * (interest_rate/100))
            print('Interest Amount : ',interest)

