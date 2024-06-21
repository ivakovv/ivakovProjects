from function_dict import *
print('Добро пожаловать в программу!')
dictionary = {}
with open('BD_dict.txt', 'r', encoding = 'utf-8') as f:
    while True:
        s = f.readline()
        if not s:
            break
        help_list = s.split('-')
        key = help_list[0]
        value = []
        for i in range(1, len(help_list)):
            if i % 2 == 0:
                value.append({help_list[i - 1]: int(help_list[i])})
        dictionary[key] = value
with open('soviet authors.txt', 'r', encoding = 'utf-8') as f:
    s = f.readline()
    soviet_authors = s.split(',')[:-1]
with open('russian authors.txt', 'r', encoding = 'utf-8') as f:
    s = f.readline()
    russian_authors = s.split(',')[:-1]
with open('foreign authors.txt', 'r', encoding = 'utf-8') as f:
    s = f.readline()
    foreign_authors = s.split(',')[:-1]
summa_pages_soviet_authors = 0
summa_pages_russian_authors = 0
summa_pages_foreign_authors = 0
summa_literary_work_soviet = 0
summa_literary_work_russian = 0
summa_literary_work_foreign = 0
while True:
    print()
    print('Выберите способ работы со словарем:\n'
    '1.Просмотр всех записей в словаре\n'
    '2.Добавление N записей\n'
    '3.Удаление записи по ключу\n'
    '4.Поиск необходимой информации\n'
    '5.Вывести список авторов(советских, русских, зарубежных)\n'
    '6.Вывести количество произведений\n'
    '7.Вывести количество сраниц\n'
    '8.Завершить работу со словарём')
    while True:
        try:
            menu = int(input('Способ №:\n'))

            break
        except ValueError:
            print('Введен некоректный способ!')
            print('Выберите способ работы со словарем:\n'
                  '1.Просмотр всех записей в словаре\n'
                  '2.Добавление N записей\n'
                  '3.Удаление записи по ключу\n'
                  '4.Поиск необходимой информации\n'
                  '5.Вывести список авторов(советских, русских, зарубежных)\n'
                  '6.Вывести количество произведений\n'
                  '7.Вывести количество сраниц у авторов\n'
                  '8.Завершить работу со словарём')
    if menu == 1:
        viewing_entries(dictionary)
    elif menu == 2:
        append_entry(dictionary, soviet_authors, foreign_authors, russian_authors)
    elif menu == 3:
        del_entry(dictionary, soviet_authors, foreign_authors, russian_authors)
    elif menu == 4:
        information(dictionary)
    elif menu == 5:
        while True:
            try:
                answer_print = int(input('Список каких авторов вы хотите вывести?\n'
              '1.Советских\n'
              '2.Русских\n'
              '3.Зарубежных\n'))
                break
            except ValueError:
                print('Введен некоректный выбор!')
        while answer_print != 1 and answer_print != 2 and answer_print != 3:
            try:
                answer_print = int(input('Такого варианта нет, поробуйте ещё раз:\n'))
                break
            except ValueError:
                print('Введен некоректный выбор!')
        if answer_print == 1:
            authors = soviet_authors
            print_authors(authors)
        elif answer_print == 2:
            authors = russian_authors
            print_authors(authors)
        elif answer_print == 3:
            authors = foreign_authors
            print_authors(authors)
    elif menu == 6:
        summa_literary_work(dictionary, soviet_authors, foreign_authors, russian_authors, summa_literary_work_soviet,
                            summa_literary_work_russian, summa_literary_work_foreign)
    elif menu == 7:
        summa_page(dictionary, soviet_authors, foreign_authors, russian_authors, summa_pages_soviet_authors,
                   summa_pages_russian_authors, summa_pages_foreign_authors)
    elif menu == 8:
        print('Спасибо, что воспользовались программой, до свидания!')
        break
    else:
        print('Такого способа нет!')
