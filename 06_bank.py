class Bank:
   bank_name = "State Bank"

   @classmethod 
   def change_bank_name(cls, name):
       cls.bank_name = name

b1 =Bank()

print(b1.bank-name)
Bank.change_bank_name("New bank")
print(b1.bank_name)