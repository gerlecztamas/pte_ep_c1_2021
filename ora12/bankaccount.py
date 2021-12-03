class BankAccount:
    def __init__(self,name: str,account_number: str, balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def kiiras(self):
        print(self.balance)

    def befizetes(self,amount: int):
        self.balance+=amount

    def felvetel(self,amount: int):
        if self.balance>=amount:
            self.balance-=amount
            print("Sikeres pénzfelvétel")
        else:
            print("Sikertelen pénzfelvétel")

account1=BankAccount("bela","0000000",100000)
account2=BankAccount("zoli","1111111")
account1.kiiras()
account2.kiiras()
account1.felvetel(50000)
account2.felvetel(50000)
account1.kiiras()
account2.kiiras()
account1.befizetes(20000)
account2.befizetes(20000)
account1.kiiras()
account2.kiiras()