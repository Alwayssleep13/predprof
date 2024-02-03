from datetime import date
'''импортируем datetime для удобного поиска и сравнения
spis - список списков с данными из предоставленного файла
word - еременная в которой лежит переданное значение'''
spis = [st[:-1].split('#') for st in open('scientist.csv', 'r', encoding='UTF-8')]
word = input()
while word != 'эксперимент':
    f = True
    for elem in spis[1:]:
        d, m, y = [int(x) for x in word.split('.')]
        indate = date(y, m, d)    # переменная, в которой лежит переданное время
        year, mounth, day = [int(x) for x in elem[2].split('-')]
        dat2 = date(year, mounth, day)    # здесь находится дата из списка ученых
        if dat2 == indate:
            sername, name, fname = elem[0].split()   # ФИО ученого
            print(f'Ученый {sername} {name[0]}.{fname[0]}. создал препарат: {elem[1]} - {elem[2]}')
            f = False
    if f:
        print('В этот день ученые отдыхали')
    word = input()
'''данный цикл сравнивает переданное значение с имеющимися в файле, выдавая требуемый ответ,
работает пока не введут слово "эксперимент"'''