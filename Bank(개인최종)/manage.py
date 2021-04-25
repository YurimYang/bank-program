from .account import *
class Manage:
    def __init__(self):
        self.accountlist = []
    def makeAccount(self):
        number = input("계좌번호 : ")
        if self.numbercheck(number):
            username=input("이름 : ")
            userbalance = int(input("예금금액 : "))
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
        return True
    def deposit(self):
        number=input("입금하실 계좌번호를 입력하세요: ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getnumber() == number:
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                self.accountlist[i].deposit(int(input("입금하실 금액을 입력해주세요 :")))
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                break
            else:
                print("존재하지 않는 계좌번호입니다.")
    def withdraw(self):
        number=input("계좌번호를 입력하세요 : ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getnumber() == number:
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                self.accountlist[i].withdraw(int(input("출금하실 금액을 입력해주세요 :")))
                print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
                break
            else:
                print("존재하지 않는 계좌번호입니다.")
    def showAccount(self):
        for i in range(len(self.accountlist)):
            print("계좌번호:",self.accountlist[i].getnumber(),"이름",self.accountlist[i].getname(),"잔액",self.accountlist[i].getbalance())
    def delete(self):
        number=input("계좌 번호를 입력하세요. :")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getnumber() == number:
                del(self.accountlist[i])
                print("계좌를 삭제하였습니다.")
            else:
                print("삭제하고자 하는 계좌번호가 맞지 않습니다.")