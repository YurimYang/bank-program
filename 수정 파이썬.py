class Account:
    def __init__(self, number,name , balance):
        self.__number = number
        self.__name = name
        self.__balance = balance

    def getnumber(self):
        return self.__number

    def getname(self):
        return self.__name

    def getbalance(self):
        return self.__balance
    
    def deposit(self,money):
        print(money,"원이 입금되었습니다.")
        self.__balance = self.__balance+money
        print("현재 잔액= ",self.__balance)
    def withdraw(self,money):
        if self.__balance<money:
            print("출금하실 금액이 부족합니다")
        else:
            print(money,"원이 출금되었습니다.")
            self.__balance=self.__balance-money
            print("현재 잔액 = ",self.__balance)
class Manage:
    def __init__(self):
        self.accountlist = []
    def makeAccount(self):
        number = input("계좌번호 : ")
        if self.numbercheck(number):
            username=input("이름 : ")
            usesrbalance = int(input("예금금액 : "))
            self.accountlist.append(Account(number,username,userbalance))
            print("##계좌 개설을 완료하였습니다##")
        else:
            print("생성 할수 없습니다.")
    def numbercheck(self,number):
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getnumber == number:
                print("중복된 계좌번호가 존재합니다.")
                return False
            return True
    def deposit(self):
        name=input("입금하실 계좌번호를 입력하세요: ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getnumber() == number:
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                self.accountlist[i].deposit(int(input("입금하실 금액을 입력해주세요 :")))
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                break
            else:
                print("존재하지 않는 계좌번호입니다.")
    def withdraw(self):
        name=input("계좌번호를 입력하세요 : ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getnumber() == number:
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                self.accountlist[i].deposit(int(input("출금하실 금액을 입력해주세요 :")))
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                break
            else:
                print("존재하지 않는 계좌번호입니다.")
    def showAccount(self):
        for i in range(self.accountlist):
            print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())

class System:
    a=Manage()
    while True:
        num=int(input("====== Bank menu ======\n 1.계좌개설\n 2.입금하기\n 3.출금하기\n 4.전체조회\n 5.종료하기\n==============\n"))
        if num==1:
            print("======계좌개설======")
            a.makeAccount()
        elif num==2:
            a.deposit()
        elif num==3:
            a.withdraw()
        elif num==4:
            a.showAccount()
        elif num==5:
            print("      프로그램이 종료됩니다      ")
            break
if __name == "__main__":
    System()
            
        
