class calculator():
    def summa():
        print(x+y)
    def sub():
        print(x-y)
    def div():
        print(x/y)
    def mult():
        print(x*y)
x = int(input("Введите число 1"))
y = int(input("Введите число 2"))
z = input("Введите действие =")
if z=='+':
    calculator.summa()
if z=='-':
    calculator.sub()
if z=='/':
        calculator.div()
if z=='*':
    calculator.mult()