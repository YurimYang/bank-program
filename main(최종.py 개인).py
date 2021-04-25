from Bank.manage import *
from Bank.account import *
class System:
    a=Manage()
    while True:
        num=int(input("====== Bank menu ======\n 1.계좌개설\n 2.입금하기\n 3.출금하기\n 4.전체조회\n 5.계좌삭제\n 6.종료하기\n ==============\n"))
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
            a.delete()
        elif num==6:
            print("      프로그램이 종료됩니다      ")
            break
        else:
            print("잘못 입력하셨습니다.")
if __name__ == "__main__":
    System()
            
