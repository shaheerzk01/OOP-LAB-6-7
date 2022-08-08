# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:08:08 2021

@author: 21A-003-SE
"""

class Account:
    
    def __init__(self, idd=0, balance = 100, annual_interest_rate=0):
        self.__idd = idd
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate
        
    def get_idd(self):
        return self.__idd
    
    def get_balance(self):
        return self.__balance
    
    def get_annual_interest_rate(self):
        return self.__annual_interest_rate
    
    def set_idd(self, new_idd):
        if isinstance(new_idd, int):
            self.__idd  = new_idd
        else:
            print("Enter valid data")
            
    def set_balance(self, new_balance):
        if isinstance(new_balance, float):
            self.__balance  = new_balance
        else:
            print("Enter valid data")
            
    def set_annual_interest_rate(self, new_annual_interest_rate):
        if isinstance(new_annual_interest_rate, float):
            self.__annual_interest_rate  = new_annual_interest_rate
        else:
            print("Enter valid data")
            
    def get_monthly_interest_rate(self):
        monthly_interest_rate  = (self.__annual_interest_rate/12)/100
        return monthly_interest_rate
        
    def get_monthly_interest(self):
        monthly_interest = self.__balance*self.get_monthly_interest_rate()
        return monthly_interest
        
    def with_draw(self, amount):
        self.__balance - amount
        
    def deposit(self, amount):
        self.__balance + amount
        
def main():
    
    account1 = Account()
    account1.set_idd(1122)
    account1.set_balance(20000.0)
    account1.set_annual_interest_rate(4.5)
    account1.with_draw(2500)
    account1.deposit(3000)
    print(account1.get_idd(), ",", account1.get_balance(), ",", account1.get_monthly_interest_rate(), ",", account1.get_monthly_interest())
    
main()