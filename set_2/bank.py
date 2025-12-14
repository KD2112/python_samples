acc={}
class bank:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
        acc[self.acc_no]=self
    def __add__(self,amount):
        self.balance+=amount
        return f"amount added"
    def withdraw(self,amount):
        self.balance-=amount
    def get_balance(self):
        # print("name:{} balance:{}".format(self.name,self.balance))
        balance=self.get
        print("balance")

acc = bank("Kalidas", 1000,2000)
acc+500

acc.get_balance()
