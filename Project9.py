log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

def get_value_from_strings(strings, spliting, name_key):
    value = None
    for element in strings:
        element = element.split(spliting)
        if element[0] == name_key:
            value = element[1]
            break
    return value

log = log.split('\n')
log_finish = []

for strings in log:
    dict_str = {
        'name': ' ',
        'gender': '',
        'item': '',
        'item_cost': 0
            }
    
    strings = strings.split(';')
    dict_str['name'] = get_value_from_strings(strings, ':', 'name')
    dict_str['gender'] = get_value_from_strings(strings, ':', 'gender')
    dict_str['item'] = get_value_from_strings(strings, ':', 'item')
    dict_str['item_cost'] = get_value_from_strings(strings, ':', 'item_cost')
    
    log_finish.append(dict_str)
    # print(log_finish)

cheep_item = []
cheep_cost = 0
for elements in log_finish:
    for k, v in elements.items():
        if k == 'item_cost' and int(v) < 13000 and not elements['item'] in cheep_item:
            cheep_cost += 1
            cheep_item.append(elements['item'])
print(f'''Количество предметов, стоящих меньше 13000 = {cheep_cost}
Предметы: {cheep_item}''')
