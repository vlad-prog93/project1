# использованные слова: яблоко, морковка, студент
#
#
def plutal_form(quantity,  form_word_1, form_word_2, form_word_3):
    lists = []
    quantity = str(quantity)
    for i in quantity:
        i = int(i)
        lists.append(i)
    if lists[-1] == 1:
        if lists[-2:] == [1,1]:
            print(f'{quantity} {form_word_3}')
        else:
            print(f'{quantity} {form_word_1}')
    elif lists[-1] in range(2, 5):
        if lists[-2:] == [1, 2] or lists[-2:] == [1, 3] or lists[-2:] == [1, 4]:
            print(f'{quantity} {form_word_3}')
        else:
            print(f'{quantity} {form_word_2}')
    else:
        print(f'{quantity} {form_word_3}')

plutal_form(48, "яблоко", "яблока", "яблок")
plutal_form(11, "студент", "студента", "студентов")