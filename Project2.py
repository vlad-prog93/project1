
password = input('Введите пароль: ')



try:                                        
 type(password[0])                            # проверка на пустой пароль
 password = int(password)                     # проверка на пароль, состоящий только из цифр
 print('Ваш пароль состоит только из цифр')   
except IndexError:                            # если ввел пустой пароль
 print('Вы ввели пустой пароль')
except ValueError:                            # соблюдены правила ввода пароля 
 print('Требования к паролю соблюдены')