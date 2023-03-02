class
def value(amount,comment,date):
    # return amount,comment,date
     x=(amount,comment,date)
     # summ.appdend=summ()
     print(x)
# x=value(gd,sg,adg)
def addet_values():
    x=list(value(input("введите сумму"),input("введите коментарий"),input("введите дату")))
    return x
if_questin=input("хотите добавить данные")
if if_questin == "да":
    x=addet_values()
if_questin=input("хотите добавить данные")
if if_questin == "да":
    x=addet_values()
else:
    result_value()
lists = []
def result_value():
    for result in x:
        print (result)