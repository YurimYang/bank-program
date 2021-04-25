user = []
class Account:
        def __init__(self,number="", name="", balance=0):
            if(number == ""):
                self.number = int(input("계좌번호: "))
                self.name = input("이름: ")
                self.balance = int(input("예금: "))
            else:
                self.number = number
                self.name = name
                self.balance = balance
                
        def print_info(self):
                print("계좌번호: ", self.number)
                print("이름: ", self.name)
                print("예금: ", self.balance)


        def getnum(self):
            return self.number 
        
        def deposit(self,money):
            self.balance += money
            return self.balance
        
        def withdraw(self,money):
            if self.balance< money:
                return 0
            else: 
                self.balance-= money
                return self.balance
        
        def inquiry(self):
            return self.balance
