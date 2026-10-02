class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner= owner
        self.balance=balance

    def deposit(self,amount):
        
         if amount <= 0:
             raise ValueError("Deposit is to low")        
         self.balance += amount 
           
            
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError ("Amount exceeds balance")
        self.balance -= amount

    def __str__(self):
       return f"{self.owner}:${self.balance}"

acc = BankAccount("Arham", 100)
print(acc)              
acc.deposit(50)
print(acc)             
acc.withdraw(30)
print(acc)              

