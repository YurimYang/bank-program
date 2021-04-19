import random
user = []
def start():
    while True:
        print("[Bank Menu]")
        print("1. 계좌개설\n2. 입금하기\n3. 출금하기\n4.전체조회\n5. 프로그램 종료")
        a= int(input("선택 = "))
        if a== 1:
            print("=================계좌개설==============")
            user.append(Account())
            print("계좌개설이 완료되었습니다.")
        elif a==2:
            print("===================입금하기==============")
            _id = input("입금할 계좌번호를 입력해주세요.")
            errorcheck(_id)
            mini_db(_id)
            ad = int(input("입금할 금액을 입력하세요."))
            deposit(_id,ad)
            print("입금이 완료되었습니다.")
            mini_db(_id)
            print("=============================================")
        elif a==3:
            print("================출금하기=================")
            _id=input("출금할 금액을 입력하세요.")
            print("계좌를 조회합니다")
            errorcheck(_id)
            mini_db(_id)
            su = int(input("출금할 금액을 입력하세요."))
            withdraw(_id,su)
            mini_db(_id)
            print("================================================")
        elif a==4:
            print("===============전체조회==================")
            if len(user) != 0:
                mini_db("all")
            else:
                print("결과가 없습니다.")
            print("==================================================")
        elif a==5:
            print("종료합니다.")
def errorcheck(_id):
    try:
        co = -1
        for i in range(0,len(user)+1):
            co = co+1
            if user[i]._id == _id:
                print("계좌를 조회합니다")
    except:
        print("없는 계좌번호 입니다.")
        start()
def deposit(_id,ad):
    co = -1
    for i in range(0,len(user)+1):
        co= co+1
        if user[i]._id == _id:
            break
        if user[co]._id == _id:
            user[i].balance += ad
def withdraw(_id,su):
    co = -1
    for i in range(0,len(user)+1):
        co = co+1
        if user[i]._id == _id:
            break
    if user[co]._id == _id:
        if user[i].balance >=su:
            user[i].balance -= su
            print("출금이 완료되었습니다.")
        else:
            print("금액이 모자랍니다.")
def mini_db(_id):
    if _id == "all":
        for i in range(0,len(user)):
            print(i+1,end= " ")
            user[i].disp()
        return
    else:
        for i in range(0,len(user)):
            if user[i]._id == _id:
                print(i+1,end=" ")
                user[i].disp()
        return True
    return False
class Account:
    def __init__(self):
        ran_num = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
        for i in range(14):
            ran_num[i] = random.randrange(1,9,1)
        ran_num[0]="1"
        ran_num[1]="1"
        ran_num[2]="0"
        ran_num[3]="-"
        ran_num[7]="-"
        self.id=""
        for i in range(14):
            self.id += str(ran_num[i])
        for i in range(0,len(user)):
            if user[i].id == self.id:
                user.append(Account())
        print(self.id, sep="")
        self.name=input("이름 입력 : ")
        self.balance = int(input("입금 금액 입력: "))
        def set_id(self,_id):
            self._id = _id
        def setname(self,name):
            self.name= name
        def setbalance(self,balance):
            self.balance = balance
        def disp(self):
            print(self._id," ",self.name," ",self.balance)

if __name__ == "__main__":
    start()
