class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0)-> None:
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def getMonthlyInterestRate(self):
        return self.getAnnualInterestRate() / 100 / 12
    
    def getMonthlyInterest(self):
        return self.getBalance() * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        self.__balance -= amount
    
    def deposit(self, amount):
        self.__balance += amount