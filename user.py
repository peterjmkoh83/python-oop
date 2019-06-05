class User:
     def __init__(self, name, email):
          self.name = name
          self.email = email
          self.account_balance = 0

     def make_deposit(self, amount):
          self.account_balance += amount
     
     def make_withdrawl(self, amount):
          self.account_balance -= amount
     
     def display_user_balance(self):
          print(self.account_balance)
     
     def transfer_money(self, other_user, amount):
          self.account_balance -= amount
          other_user.account_balance += amount
          
          

          

user1 = User("John", "john@gmail.com")
user2 = User("Heidi", "heidi@gmail.com")
user3 = User("Paul", "paul@gmail.com")

user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(200)
user1.make_withdrawl(200)
user1.transfer_money(user3, 100)

user2.make_deposit(300)
user2.make_deposit(200)
user2.make_withdrawl(200)
user2.make_withdrawl(200)

user3.make_deposit(500)
user3.make_withdrawl(200)
user3.make_withdrawl(200)

user1.display_user_balance()
user2.display_user_balance()
user3.display_user_balance()

