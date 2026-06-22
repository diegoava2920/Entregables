class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        pass

    def add_money(self, additional):
        self.balance = self.balance + additional
        print (f"Dinero agregado\nNuevo valor {self.balance}")

    def remove_money(self, removal):
        new_total = self.balance - removal
        return new_total
    
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.min_balance = 100
        super().__init__(balance)
    
    def remove_money(self, removal):
        print (f"\nDinero a retirar\n{removal}")
        new_total = self.balance - removal
        if new_total > self.min_balance:
            self.balance = new_total
            print (f"\nDinero retirado\nNuevo valor {self.balance}")
        else:
            print("\nEl retiro excede el minimo de balance\n")

Ahorros = SavingsAccount(1000)

Ahorros.add_money(500)

Ahorros.remove_money(1300)

Ahorros.remove_money(200)