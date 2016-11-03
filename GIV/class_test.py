# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:08:28 2016

@author: kiawo
"""

# Class Tutorial

class Customer():
    
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:
        Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
    def __init__(self, name, balance =0.0):  
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance')
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        self.balance += amount
        return self.balance

kia = Customer('Kia Naziri', 1000.00)

kia.balance    
kia.name        
kia.withdraw(300)
kia.deposit(500)

#===CAR

class Car(object):
    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model
    @staticmethod
    def make_car_sound():
        print ('VRoooooommmm!')
    
mustang = Car('Ford', 'Mustang')

print (mustang.wheels)
