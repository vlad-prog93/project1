
# создание аккаунтов для пользователей
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# создание пользователей
user1 = {'name':'Иван', 'age': 20, 'account': account1}
user2 = {'name':'Петр', 'age': 25, 'account': account2}
user3 = {'name':'Ольга', 'age': 18, 'account': account3}
user4 = {'name':'Анна', 'age': 21, 'account': account4}

# объединение пользователей в один список
user_list = [user1, user2, user3, user4]

# поиск пользователей по имени или аккаунту
name_account = input('Введите ключ (name или account): ')
print('')

# привести введенные данные к нижнему регистру
name_account = name_account.lower()

# посчитать количество пользователей
count_users = len(user_list)

# вывод пользователей (name или account)
for i in range(count_users):
 name_user = user_list[i][name_account]
 try:
  print(f'Значение ключа account для пользователя {i+1}: {name_user["login"]}','\n')
 except TypeError:
  print(f'Значение ключа name для пользователя {i+1}: {name_user}','\n')

# выбор пользователя
try:
 count_number = int(input('Введите порядковый номер пользователя (от 1 до 4): '))
 print('')
 years = (user1["age"] + user2["age"] + user3["age"] + user4["age"])/2
 print(f'Среднее значение возраста: {years} ')
 choose_user = user_list[count_number - 1]
 print(f'''

Вы выбрали пользователя {choose_user["name"]} 
возраст: {choose_user["age"]} лет 
логин: {choose_user["account"]["login"]}
пароль: {choose_user["account"]["password"]} 

''')
 # выбираем пользователя, которого нужно поставить в конец списка
 try:
  last_user = int(input('Введите номер пользователя, которого нужно переместить в конец списка? : '))
  print('')
  last_user = last_user - 1
  print('''   Было:  ''')
  print(f"{user_list}'\n'")
# ставим пользователя в конец списка
  delete = user_list.pop(last_user)
  print(f'Перемещаем {delete} в конец списка')
  user_list.append(delete)
  print(''' 
  Стало:    
  ''')
  print(user_list)
 except:
  print('Пользователь с указанным номером не найден')



# если ввел больше 4
except IndexError:
 print('С таким номером пользователя нет')
# если ничего не ввел
except ValueError:
 print('\n','Вы ничего не ввели')

input('Нажмите любую клавишу для выхода из программы')
