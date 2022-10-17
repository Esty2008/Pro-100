from copyreg import pickle


class ATM(object):
    def __init__(self,cardNumber,pinNumber,balance):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.balance=balance
    def CashWithdrawl(self):
        print(self.cardNumber, self.pinNumber)
        print("235$ dollars have been withdrawn")
    def currentBalance(self):
        print(self.balance)

ATMObj=ATM(346965245173, 7189, 5500 )

ATMObj.CashWithdrawl()
ATMObj.currentBalance()