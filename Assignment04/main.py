class Bank:
    bank_name = "Code Bank" 

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Bank Name:", Bank.bank_name)

acc1 = Bank("CodeQueen")
acc2 = Bank("Anusha Bank")

acc1.display()
acc2.display()

print("\nChanging bank name...\n")
Bank.change_bank_name("Meezan Bank")

acc1.display()
acc2.display()
