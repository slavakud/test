
class Callories():
    x=0
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date

        Callories.summ(self)

    def __str__(self):
        return f"{Callories.x}"

    def print_name(self):
        print(self.amount,self.comment,self.date,)

    def summ(self):
        Callories.x+=int(self.amount)



r1 = Callories(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Callories(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Callories(amount=691, comment="Катание на такси", date="08.03.2019")
name=[r1,r2,r3]
t=0
i=3
while t ==0:
    if input("Хотите добавить данные?")=="да":
        name.append(input ("Введите имя переменной"))
        name[i]=Callories(int(input ("Введите amount")),input ("Введите comment"),input ("Введите date"))
        i+=1
    else:t=1
for values in name:
    Callories.print_name(values)




