def viewing_entries(dictionary):
    for key, value in dictionary.items():
        print(key, end=' ')
        for i in value:
            for key1, value1 in i.items():
                print(f'"{key1}"', '-', value1, 'стр.',end = '\t')
        print()
def append_entry(dictionary, soviet_authors, foreign_authors, russian_authors):
    while True:
        try:
            n = int(input('Введите количество записей, которые хотите добавить:\n'))
            break
        except ValueError:
            print('Введено некорректное количество записей!')
    for i in range(n):
        author = input('Введите фамилию автора:\n').capitalize().strip()
        book = input('Введите название произведения:\n').strip()
        while True:
            try:
                page = int(input('Введите кол-во страниц:\n'))
                break
            except ValueError:
                print('Введено неверное кол-во страниц!')
        while True:
            try:
                author_help = int(input('Какой это автор?\n'
                                '1.советский\n'
                                '2.русский\n'
                                '3.зарубежный\n'))
                break
            except ValueError:
                print('Введен некорректный пункт!')
        while author_help != 1 and author_help != 2 and author_help != 3:
            while True:
                try:
                    author_help = int(input('Такого пункта нет! Повторите попытку\n'
                                        '1.советский\n'
                                        '2.русский\n'
                                        '3.зарубежный\n'))
                    break
                except ValueError:
                    print('Введен некорректный пункт!')
        if author_help == 1:
            if author not in soviet_authors:
                soviet_authors.append(author)
        elif author_help == 2:
            if author not in russian_authors:
                russian_authors.append(author)
        else:
            if author not in foreign_authors:
                foreign_authors.append(author)
        if author in dictionary.keys():
            dictionary[author].append({book: page})
        else:
            value = [{book: page}]
            dictionary[author] = value
def summa_page(dictionary,soviet_authors, foreign_authors, russian_authors, summa_pages_soviet_authors, summa_pages_russian_authors, summa_pages_foreign_authors):
    for key, value in dictionary.items():
        for i in value:
            for key1, value1 in i.items():
                if key in soviet_authors:
                    summa_pages_soviet_authors += value1
                elif key in russian_authors:
                    summa_pages_russian_authors += value1
                elif key in foreign_authors:
                    summa_pages_foreign_authors += value1
    print(f'Количество страниц советских произведений:{summa_pages_soviet_authors}')
    print(f'Количество страниц русских произведений:{summa_pages_russian_authors}')
    print(f'Количество страниц русских произведений:{summa_pages_foreign_authors}')
    print(f'Всего проиведений:{summa_pages_soviet_authors + summa_pages_russian_authors + summa_pages_foreign_authors}')
def del_entry(dictionary, soviet_authors, foreign_authors, russian_authors):
    del_author = (input('Введите автора, которого хотите удлаить:\n').capitalize().strip())
    while dictionary.get(del_author) == None:
        del_author = input('Такого автора нет. Попробуйте ещё раз:\n')
    dictionary.pop(del_author)
    if del_author in soviet_authors:
        soviet_authors.remove(del_author)
    elif del_author in foreign_authors:
        foreign_authors.remove(del_author)
    elif del_author in russian_authors:
        russian_authors.remove(del_author)
def information(dictionary):
    info_answer = 'да'
    while info_answer == 'да':
        while True:
            try:
                search_parameter = int(input('Параметры поиска:\n'
                                    '1.Поиск по автору\n'
                                    '2.Поиск по книге\n'))
                break
            except ValueError:
                print('Введен некорректный выбор!')
        if search_parameter == 1:
            Flag = False
            author = input('Введите фамилию автора :\n').strip()
            for key, value in dictionary.items():
                if author.lower() in key.lower():
                    print(key, end=' ')
                    for i in value:
                        for key1, value1 in i.items():
                            print(f'"{key1}"', '-', value1, 'стр.', end='\n')
                            Flag = True
                            break
            if Flag == False:
                print('Такого автора нет!')
        elif search_parameter == 2:
            Flag = False
            book = input('Введите название книги:\n').strip()
            for key, value in dictionary.items():
                    for i in value:
                        for key1, value1 in i.items():
                            if key1.lower() == book.lower():
                                print(key, end=' ')
                                print(f'"{key1}"', '-', value1, 'стр.', end='\n')
                                Flag = True
                                break
                            else:
                                continue
                        continue
                    continue
            if Flag == False:
                print('Такой книги нет!')
        else:
            print('Выбран непрпаильный параметр поиска!')
        info_answer = input('Продолжить поиск?(да или нет)\n').lower().strip()
        while info_answer != 'да' and info_answer != 'нет':
            info_answer = input(('Введен неправильный ответ, повторите попытку:\n')).lower().strip()
def print_authors(authors):
    print(*authors, sep=', ')
def summa_literary_work(dictionary, soviet_authors, foreign_authors, russian_authors, summa_literary_work_soviet, summa_literary_work_russian, summa_literary_work_foreign):
    for key, value in dictionary.items():
        if key in soviet_authors:
            summa_literary_work_soviet += len(value)
        elif key in russian_authors:
            summa_literary_work_russian += len(value)
        elif key in foreign_authors:
            summa_literary_work_foreign += len(value)
    print(f'Всего советских проиведений:{summa_literary_work_soviet}')
    print(f'Всего русских проиведений:{summa_literary_work_russian}')
    print(f'Всего зарубежных проиведений:{summa_literary_work_foreign}')
    print(f'Всего проиведений:{summa_literary_work_foreign + summa_literary_work_russian + summa_literary_work_soviet}')
