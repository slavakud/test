# with open("password.txt") as f:
#     password_list = f.read()
# print (password_list)
# password=input('Введите пароль')
# print (len(password))
# if len(password)<=6 or password in password_list:
#     print ("Пароль слишком легкий ")
# else: print("пароль принят")
def test (name,isEnemy):
    if isEnemy:
        print(isEnemy)
    else: print (f"is not true is {isEnemy}")
test("Jack",False)