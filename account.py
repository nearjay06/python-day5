class BankAccount:
    
 def __init__(self):
  self.balance=0
  self.status= True
  
 def open(self):
   pass

 def get_balance(self):
    if self.status == False:
     raise ValueError('Account Closed')
    return self.balance

 def deposit(self,amount):
  if amount <= 0:
     raise ValueError('try again')

  self.balance += amount

  if self.status==False:
     raise ValueError ('Closed Account')

  self.balance -+ amount
  if amount >= self.balance:
     return self.balance

 def withdraw(self,amount):
  if self.status == False:
   raise ValueError ('Account Closed')
  if amount <0:
   raise ValueError ('Insufficient Funds')

  self.balance -= amount

  if amount >self.balance:
   raise ValueError ('Cannot withdraw')

  self.balance += amount
  if amount >=self.balance:
   return self.balance


 def close(self):
    self.status = False  
   

 


    
   