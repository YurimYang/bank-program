class Account:
    def __init__(self,userid=None,username=None,userbalance=None):
        self.__userid = userid
        self.__username = username
        self.__userbalance = userbalance
    def getUserid(self):                                      
        return self.__userid
    def getUserName(self):
        return self.__username
    def getUserbalance(self):
        return self.__userbalance    
    def deposit(self,money):             
        print(money,'원이 입금되었습니다.')
        self.__userbalance = self.__userbalance+money 
        print("현재 잔액 = ",self.__userbalance)
    def withdraw(self,money):      
        if self.__userbalance<money:
            print("출금할 금액이 잔여 금액",self.__userbalance,"보다 많습니다.")
        else:
            print(money,"원이 출금되었습니다.")
            self.__userbalance = self.__userbalance-money
            print("현재 잔액 = ",self.__userbalance)
class BankManager:
    def __init__(self):
        self.accountlist = []
    def makeAccount(self): 
        userid = input("계좌번호 : ")
        if self.idcheck(userid):
            username = input("이름 = ")
            userbalance =int(input("예금금액 ="))  
            self.accountlist.append(Account(userid,username,userbalance))
            print("##계좌 개설을 완료하였습니다##")
        else:
            print("생성할 수 없습니다.")
    def idcheck(self,userid):
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getUserid == userid:
                print("중복된 계좌번호가 존재합니다.")
                return False
        return True
    def deposit(self):   
        userid=input("계좌번호를 입력하세요 : ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getUserid() == userid:
                self.accountlist[i].deposit(int(input("입금할 금액을 입력해주세요 :")))
                break
            else:
                print("계좌를 찾을수 없습니다.")
    def withdraw(self): 
        userid=input("계좌번호를 입력하세요 = ")   
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getUserid() == userid:
                self.accountlist[i].withdraw(int(input("출금할 금액을 입력해주세요 =")))
                break
            else:
                print("계좌를 찾을수 없습니다.")                  
    def showAccount(self): 
        for i in range(len(self.accountlist)):
            print("계좌번호 = ",self.accountlist[i].getUserid(),"고객이름 = ",
                  self.accountlist[i].getUserName(),"현재 잔액 = ",self.accountlist[i].getUserbalance())

class BankingSystem:
        a=BankManager()
        while True:
            num=input(" ======== Bank Menu ========\n 1.계좌개설\n 2.입금하기\n 3.출금하기 \n 4.전체조회 \n 5.종료하기")
            print()
            if num=="1":
                print("============================")                
                a.makeAccount()         
                print(" ============================")
            elif num=="2":
                print(" ============================")
                a.deposit()
                print(" ============================")
            elif num=="3":
                print(" ============================")               
                a.withdraw()
                print(" ============================")             
            elif num=="4":
                print(" ============================")             
                a.showAccount()
                print(" ============================")               
            elif num=="5":
                print(" ============================")
                print("     프로그램이 종료됩니다   ")
                print(" ============================")
                break
if __name__ == '__main__':
    BankingSystem()

