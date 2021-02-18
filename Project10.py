import pandas as pd
import openpyxl
import os
import collections as col


# Извлекаем в список информацию из logs.xlsx, Excel файла
pandas_dictionary = pd.read_excel('logs.xlsx', sheet_name='log', engine='openpyxl')
list_dictionary = pandas_dictionary.to_dict(orient = 'records')

# Генерируем и приводим к списку купленные товары или браузер
def products(row):
    # делаем переменную goods (названия самых продаваемых товаров) глобальной
    global goods
    if row == 'Купленные товары':
        # отбираем колонку "купленные товары" 
        products = [list_dictionary[i][row] for i in range(0, len(list_dictionary))]
    
        # Преобразуем к удобному нам виду
        list_in_list_products = [j.split(',') for i in products for j in i.split(',')]
        str_in_list_products = []
        for i in list_in_list_products:
            str_in_list_products.append(i[0])

        # Фильтруем купленные товары - убираем "Еще 2 варианта" и "Еще 3 варианта"
        filter_product = list(filter(lambda x: x != 'Ещё 2 варианта' and x != 'Ещё 3 варианта', 
                                str_in_list_products))

        # Отсортировать купленные товары с помощью библиотеки collection
        count_product = col.Counter(filter_product)
        count_product = count_product.most_common(7)
    elif row == 'Браузер':
        products = [list_dictionary[i]['Браузер'] for i in range(0, len(list_dictionary))]

        # Отсортировать купленные товары с помощью библиотеки collection
        count_product = col.Counter(products)
        count_product= count_product.most_common(7)
    
    # Выбираем из кортежа только названия товаров
    goods = [k for k, v in count_product]

# Определяем количество продаж по месяцам    
def count(month, goods, row):
    product_sorted = [goods for i in range(0, len(list_dictionary)) 
                    if goods in list_dictionary[i][row] 
                    and list_dictionary[i]['Дата посещения'].date().month == month]
    return len(product_sorted)

# Записываем данные в Excel
def load(goods, good, row):
    # Открываем файл xlsx для записи
    book = openpyxl.load_workbook(filename = 'report.xlsx')
    sheet = book['Лист1']

    # Записываем товар в ячейку 
    sheet[row][0].value = goods

    # Записываем количество продаж в ячейки
    for i in range(2,14):
        sheet[row][i].value = good[0]
        good.pop(0)

    # Сохраняем в Excel
    book.save('report.xlsx')
    book.close()

# Генерируем и приводим к списку купленные товары фильтруем товары по полу
def male_female(sex):
    global best
    global worst

    # отбираем колонку "купленные товары" 
    products = [list_dictionary[i]['Купленные товары'] for i in range(0, len(list_dictionary)) 
                if list_dictionary[i]['Пол'] == sex]
    
    # Преобразуем к удобному нам виду
    list_in_list_products = [j.split(',') for i in products for j in i.split(',')]
    str_in_list_products = []
    for i in list_in_list_products:
        str_in_list_products.append(i[0])

    # Фильтруем купленные товары - убираем "Еще 2 варианта" и "Еще 3 варианта"
    filter_product = list(filter(lambda x: x != 'Ещё 2 варианта' and x != 'Ещё 3 варианта', 
                            str_in_list_products))

    # Отсортировать купленные товары с помощью библиотеки collection
    count_product = col.Counter(filter_product)

    best1 =  count_product.most_common()
    best = [k for k, v in best1]
    worst1 = count_product.most_common()[:-len(count_product):-1]
    worst = [k for k, v in worst1]


def load_best_worst(sex):
    # Открываем файл xlsx для записи
    book = openpyxl.load_workbook(filename = 'report.xlsx')
    sheet = book['Лист1']
    if sex == 'м':
        # Записываем товар в ячейку 
        sheet[31][1].value = best[0]
        sheet[33][1].value = worst[0]
    elif sex == 'ж':
        sheet[32][1].value = best[0]
        sheet[34][1].value = worst[0]

    # Сохраняем в Excel
    book.save('report.xlsx')
    book.close()

products('Купленные товары')
gen_count = [count(month,goods[0],'Купленные товары') for month in range(1,13)]
load(goods[0], gen_count, 19)
gen_count = [count(month,goods[1],'Купленные товары') for month in range(1,13)]
load(goods[1], gen_count, 20)
gen_count = [count(month,goods[2],'Купленные товары') for month in range(1,13)]
load(goods[2], gen_count, 21)
gen_count = [count(month,goods[3],'Купленные товары') for month in range(1,13)]
load(goods[3], gen_count, 22)
gen_count = [count(month,goods[4],'Купленные товары') for month in range(1,13)]
load(goods[4], gen_count, 23)
gen_count = [count(month,goods[5],'Купленные товары') for month in range(1,13)]
load(goods[5], gen_count, 24)
gen_count = [count(month,goods[6],'Купленные товары') for month in range(1,13)]
load(goods[6], gen_count, 25)



products('Браузер')
gen_count = [count(month,goods[0],'Браузер') for month in range(1,13)]
load(goods[0], gen_count, 5)
gen_count = [count(month,goods[1],'Браузер') for month in range(1,13)]
load(goods[1], gen_count, 6)
gen_count = [count(month,goods[2],'Браузер') for month in range(1,13)]
load(goods[2], gen_count, 7)
gen_count = [count(month,goods[3],'Браузер') for month in range(1,13)]
load(goods[3], gen_count, 8)
gen_count = [count(month,goods[4],'Браузер') for month in range(1,13)]
load(goods[4], gen_count, 9)
gen_count = [count(month,goods[5],'Браузер') for month in range(1,13)]
load(goods[5], gen_count, 10)
gen_count = [count(month,goods[6],'Браузер') for month in range(1,13)]
load(goods[6], gen_count, 11)

male_female('м')
load_best_worst('м')
male_female('ж')
load_best_worst('ж')