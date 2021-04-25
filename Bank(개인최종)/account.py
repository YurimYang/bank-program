class Account:
    def __init__(self, number, name , balance):
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
        print("현재 잔액: ",self.__balance)
    def withdraw(self,money):
        if self.__balance<money:
            print("출금하실 금액이 부족합니다")
        else:
            print(money,"원이 출금되었습니다.")
            self.__balance=self.__balance-money
            print("현재 잔액 = ",self.__balance)
    def delete(self,number):
        if self.__number==number:
            print("계좌를 삭제합니다.")
        else:
            print("삭제하고자 하는 계좌가 맞지 않습니다.")