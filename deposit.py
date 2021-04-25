user = []

class Account:
        def __init__(self,number="", name="", balance=0):
            if(number == ""):
                self.number = input("계좌번호: ")
                self.name = input("이름: ")
                self.balance = input("예금: ")
            else:
                self.number = number
                self.name = name
                self.balance = balance
                
        def print_info(self):
                print("계좌번호: ", self.number)
                print("이름: ", self.name)
                print("예금: ", self.balance)

        #def dispaly(self):
         #   return "self.number:self.name:self.balance\n"    
        #def set_Acc
        #    number = 
          #  name = input("이름: ")
           # balance = input("예금: "


        def getnum(self):
            return self.number 
        
        def deposit(self,money):
            self.balance += money
            return self.money
        
        def withdraw(self,money):
            if self.balance< money:
                return 0
            else: 
                self.balance-= money
                return money
        
        def inquiry(self):
            return self.balance


class Manage:

    def deposit(self,number):
        for i in user:
            if i.getnum() == number:
                print("계좌번호: ", self.number, "/ 이름: ", self.name, "/ 잔액: ", self.balance)
                money = int(input("입금하실 금액을 입력해주세요: "))
                plus = i.deposit(money)
                print("잔액은 {0}입니다.".format(plus))
                print("계좌번호: ", self.number, "/ 이름: ", self.name, "/ 잔액: ", plus)
                return 0
        print("오류입니다.")
    
    def withdraw(self,number):
        for i in user:
            if i.getnum() == number:
                print("계좌번호: ", self.number, "/ 이름: ", self.name, "/ 잔액: ", self.balance)
                money = int(input("출금하실 금액을 입력해주세요: "))
                minus = i.withdraw(money)
                print("계좌번호: ", self.number, "/ 이름: ", self.name, "/ 잔액: ", minus)
            print("오류입니다.")
                
    def show(self):
        if len(user) != 0:
            for i in range(0,len(user)):
                user[i].print_info()
        else:
            print("오류입니다.")

    
    def newnum(self,xnumber):
        for i in user:
            if i.getnum() == xnumber.getnum():
                return "이미 존재합니다."
        user.append(xnumber)

if __name__=="__main__":
    Manage()
    

class System:
    def run():
        while True:
            print("=====Bank Menu=====")
            print("1. 계좌개설", "2. 입금하기", "3. 출금하기", "4. 전체조회", "5. 종료하기", sep = '\n')
            print("===================")
            a = int(input())

            if a == 1 :
                print("=====계좌개설=====")
                print(Manage().newnum(Account()))
                

            elif a == 2:
                number = int(input("입금하실 계좌번호를 입력해주세요: "))
                Manage().deposit(number)
                

            elif a == 3:
                number = int(input("출금하실 계좌번호를 입력해주세요: "))
                Manage().withdraw(number)
                
            
            elif a == 4:
                Manage().show()
            
            elif a == 5:
                break

        
if __name__=="__main__":
   System.run()
