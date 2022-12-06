from pprint import pprint
from random import randint
users={
    'AlexShurikov':{'password':12345678910,'id':9285461},
    'Vova777':{'password':654647,'id':1234556678},
    'Bobik999':{'password':43343434343,'id':1234567890}
}
print(users['AlexShurikov']['password'])
# while True:
#     name=input('Имя:\n')
#     if name in users:
#         par=int(input('Введите пароль'))
#         if par == users[name]['password']:
#             print('Вы вошли в личный кабинет')
#     else:
#         print('Зарегистриcтрируйтесь, аккаунта с таким названием не найдено!')
#         name = input('Ф.И.О.:\n')
#         par = int(input('Введите пароль'))
#         par2 = int(input('Повтор пароля'))
#         if par == par2:
#             print('Вы успешно зарегистрировались')
#             users[name]= {'password':par,'id':randint(1,100)}

# # def buy():
# #     pay=0
# #     while True:
# #         enter=input('Что покупаем?:\n')
# #         if enter == 'end':
#             break
#         pay+=price[enter]
#         return pay