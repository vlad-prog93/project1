
# https://yandex.ru/search/?text=pumpskill.ru&lr=213&clid=2186621&src=suggest_B

def get_absolute_url(x, *args, **kwargs):
    lists = [x, *args, kwargs] # создал список из всех аргументов функции
    l = '' # создал пустую строку
    for i in range(0, len(lists)):
        # сравниваю типы аргументов
        if type(lists[i]) == str and type(lists[i + 1]) == str:
            l += lists[i] + '/'
        if type(lists[i]) == str and type(lists[i + 1]) == dict:
            l += lists[i] + '?'
        if type(lists[i]) == dict:
            for k, v in lists[i].items():
                l +=k + '=' + v + '&'
            l = l[0:-1]
            print(l)

get_absolute_url('www.yandex.ru','search', text='pumpskill.ru', lr='213', clid='2186621', src='suggest_B')
