'''Implement a class program to create an instance of the BankAccount class and test the deposit and withdrawl functionality'''






class BankAccount:

  def __init__(self,account_number, account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit (self, amount):
   if amount > 0:
     self.__account_balance =+ amount
    #self.__acount_balance = self.__account_balance+amount
     print("Deposited ₹{}. New balance.${}".format(amount, 
         self.__account_balance))
   else:
     print("Invalid deposit amount.please deposit a positive amount.")
    
  def withdraw(self,amount):
   if amount > 0 and amount <= self.__account_balance:
    self.__account_balance -= amount
    #self.__account_balance = self.__account_balanc - amount
    print("withdrew ₹{}. New balance: ₹{}".format(amount,
                                    self.__account_balance))
   else:
    print("Invalid withdrawal amount or insufficicent balance.")
    
  def display_balance(self):
   print("Account balance for {} (Account #{}): ₹{}".format( 
      self.__account_holder_name, self.__account_number,
      self.__account_balance))


#Create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
       account_holder_name="Hari Prabu",
       initial_balance=5000.0)

# test deposit and withdrawal functionality
account.display_balance()
account.deposit(amount=500.0)
account.withdraw(amount=2000.0)
account.withdraw(20000.0)
account.display_balance()
