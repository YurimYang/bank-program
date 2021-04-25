from account import Account
from manage import Manage

user = []
class System:

    def run():
        while True:
            print("=====Bank Menu=====")
            print("1. 계좌개설", "2. 입금하기", "3. 출금하기", "4. 전체조회", "5. 전체계좌삭제", "6. 종료하기", sep = '\n')
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
                del user[:]
                print("모든 계좌가 삭제되었습니다.")

            
            elif a == 6:
                break

        
if __name__=="__main__":
   System.run()