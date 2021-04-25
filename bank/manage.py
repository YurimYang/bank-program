user = []
class Manage:
    def deposit(self,number):
        for i in user:
            if i.getnum() == number:
                print("계좌번호: ", number, "/ 이름: ", i.name, "/ 잔액: ", i.balance)
                money = int(input("입금하실 금액을 입력해주세요: "))
                plus = i.deposit(money)
                print("계좌번호: ", number, "/ 이름: ", i.name, "/ 잔액: ", plus)
                return 0
        print("오류입니다.")
    
    def withdraw(self,number):
        for i in user:
            if i.getnum() == number:
                print("계좌번호: ", number, "/ 이름: ", i.name, "/ 잔액: ", i.balance)
                money = int(input("출금하실 금액을 입력해주세요: "))
                minus = i.withdraw(money)
                print("계좌번호: ", number, "/ 이름: ", i.name, "/ 잔액: ", minus)
                return 0
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