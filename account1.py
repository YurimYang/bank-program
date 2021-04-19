class Account(object):
        def __init__(self, number, name, deposit):
            self.number = number
            self.name = name
            self.deposit = deposit
    x = int(input("계좌번호: "))
    y =  input("이름: ")
    z = int(input("예금: "))
    DevAccount = Account(x,y,z)
