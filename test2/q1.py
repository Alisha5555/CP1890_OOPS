from dataclasses import dataclass

@dataclass
class Bank:
    accounts = {"customer_name":"balance"}
    account_number:int
    transaction_history= []
    
    def create_account(self,accounts):

    def deposit(self, customer_name, balance):


@dataclass
class SavingsAccount(Bank):
    interest_rate:float
