class Acc_man:
    def __init__(self):
        self.accounts={}
    def register(self,account):
        self.accounts[account.acc_no]=account
    def items(self):
        return self.accounts.items()
    def __getitem__(self,acc_no):
        return self.account[acc_no].balance
    def __setitem__(self,acc_no,amount):
        self.account[acc_no].balance=amount
    def __len__(self):
        return len(self.accounts)
    def __str__(self):
        return "\n".join(str(acc) for acc in self.accounts.values())
    def __contains__(self, acc_no):
        return acc_no in self._accounts

    def __iter__(self):
        return iter(self.accounts.values())
manager=Acc_man()
class Bank:
    def __init__(self,name,acc_no,amount):
        self.name=name
        self.acc_no=acc_no
        self.amount=amount

        manager.register(self)
    
    def deposit(self,amount):
        self.amount+=amount
    def withdraw(self,amount):
        self.amount-=amount
    def __repr__(self):
        return f"Bank(name={self.name}, acc_no={self.acc_no}, balance={self.amount})"

acc1=Bank("kalidas",10,2000)
acc1.deposit(100)
acc2=Bank("anakha",1,2000)
# summary={acc.acc_no:acc.amount for acc in manager}
# print(summary)

print(manager.items())

print(manager)

print(acc1)
print(acc2)

