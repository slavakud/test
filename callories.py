
class Callories():
    x=0
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date
        Callories.print_name(self)
        Callories.summ(self)

    def print_name(self):

        print(self.amount,self.comment,self.date,)

    def summ(self):
        Callories.x+=self.amount
        return Callories.x

r1 = Callories(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Callories(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Callories(amount=691, comment="Катание на такси", date="08.03.2019")

print(Callories.x)



