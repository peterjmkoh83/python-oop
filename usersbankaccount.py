from bankAccount import BankAccount

class User:
     def __init__(self, name, email):
          self.name = name
          self.email = email
          self.accounts = {
               "checking": BankAccount(0.01, 0), "saving": BankAccount(0.01, 0)
          }

     def display_info(self):
          print("Name:", self.name)
          for account in self.accounts: 
               print(f"{account}: {self.accounts[account].balance}")

     def make_deposit(self, account_type, amount):
          self.accounts[account_type].deposit(amount)

     def make_withdrawl(self, account_type, amount):
          self.accounts[account_type].withdraw(amount)     


user1 = User("John", "john@gmail.com")
user2 = User("Heidi", "heidi@gmail.com")

user1.make_deposit('checking', 100)
user1.make_deposit('saving', 1000)
user1.make_withdrawl('saving', 500)
user1.display_info()

user2.make_deposit('saving', 30000)
user2.make_deposit('checking', 10000)
user2.display_info()

