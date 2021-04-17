print("=====Bank Menu=====")
print("1. 계좌개설", "2. 입금하기", "3. 출금하기", "4. 전체조회", "5. 종료하기", sep = '\n')
print("===================")
a = int(input())

if a == 1 :
    print("=====계좌개설=====")
    class Account(object):
        def __init__(self, number, name, deposit):
            self.number = number
            self.name = name
            self.deposit = deposit

    x = int(input("계좌번호: "))
    y = str(input("이름: "))
    z = int(input("예금: "))
    DevAccount = Account(x,y,z)
    print(DevAccount.name)
    print("##계좌개설을 완료하였습니다##")
    print("=====Bank Menu=====")
    print("1. 계좌개설", "2. 입금하기", "3. 출금하기", "4. 전체조회", "5. 종료하기", sep = '\n')
    print("===================")
    a = int(input())

elif a == 2 :
    from account1 import Account
    b = int(input("입금하실 계좌번호를 입력해주세요: "))
    if b == DevAccount.number:
        print("계좌번호: ", DevAccount.number, "/ 이름: ", DevAccount.name, "/ 잔액: ", DevAccount.deposit)
        c = int(input("입금하실 금액을 입력해주세요: "))
        print("계좌번호: ", DevAccount.number, "/ 이름: ", DevAccount.name, "/ 잔액: ", DevAccount.deposit + c)
