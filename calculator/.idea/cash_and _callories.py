from decimal import Decimal
class Calculator():
    record=[]
    def __init__(self,limit_cal,currency,rub, usd,eur):
        self.currency=currency
        self.rub=rub
        self.usd=usd
        self.eur=eur
        self.limit_cal=limit_cal



class CaloriesCalculator(Calculator):
    def get_calories_remaine(self):
        print
        if self.limit_cal >= r4.amount+r5.amount+r6.amount:
            N=self.limit_cal-(r4.amount+r5.amount+r6.amount)
            print(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {N} кКал")
        else:
            print(f"Хватит есть!, если лимит достигнут или превышен")



class CashCalculator(Calculator):
    def get_today_cash_remained(self,name):
        cash= values.currency-(r1.amount+r2.amount+r3.amount)
        if cash<= 0:
            print("Лимит превышен")

        if name=="rub":
            print (f"можно купить на {cash}")

        elif name=="eur":

            print (f'можно купить на uer {round(cash/values.eur,2)}' )
        else:
            print (f'можно купить на usd {round(cash/values.usd,2)}')

class Record():
    def __init__(self,amount,comment,date):
         self.amount=amount
         self.comment=comment
         self.date=date

# для CashCalculator
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1060, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=140, comment="Баночка чипсов.", date="24.02.2019")
values=Calculator(2300,10000,1,75,85)
name= input("Введите валюту")
CashCalculator.get_today_cash_remained(values,name)
CaloriesCalculator.get_calories_remaine(values)