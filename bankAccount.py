class BankAccount:
     
     def __init__(self, int_rate=0.01, balance=0):
          self.int_rate = int_rate
          self.balance = balance
     
     def deposit(self, amount):
          self.balance += amount
          return self

     # if in sufficeint: print ("Insufficient funds: Charging a $5 fee") and deduct $5  use boolean if positive, withdraw; if negative, charge
     def withdraw(self, amount):
          self.balance -= amount
          if self.balance < 0:
               print("Insufficient funds: Charging a $5 fee")
               self.balance = self.balance - 5          
          else: 
               self.balance
          return self  
                   
     def display_acct_info(self):
          print("Balance: $", self.balance)
          return self

     def yield_interest(self):
          if self.balance > 0:
               interest_gains = self.int_rate * self.balance
               self.balance += interest_gains
               print("Current Balance: $", self.balance)
          else:
               self.balance
               print("Current Balance: $", self.balance)
          return self

account1 = BankAccount(.01, 100)
account2 = BankAccount(.05, 10000)

account1.deposit(300).deposit(300).deposit(300).withdraw(1100)
account2.deposit(3000).deposit(2000).withdraw(5000).withdraw(5000).withdraw(3000).withdraw(1000)
     

account1.display_acct_info()
account1.yield_interest()

account2.display_acct_info()
account2.yield_interest()


          