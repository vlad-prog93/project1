cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')

city = city.capitalize()


if tourists[0]['city'] == city: # город Лондон
 print(f'Турист {users[0]["name"]} возраст {users[0]["age"]}. Посетил город {cities[2]}')
elif tourists[1]['city'] == city: # город Москва
 print(f'Турист {users[1]["name"]} возраст {users[1]["age"]}. Посетил город {cities[0]}')
elif tourists[2]['city'] == city: # город Париж
 print(f'Турист {users[2]["name"]} возраст {users[2]["age"]}. Посетил город {cities[1]}')
else:
 print('Такого города нет в базе') 