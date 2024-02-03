from datetime import date
'''импортируем datetime для удобного поиска и сравнения
spis - список списков с данными из предоставленного файла
list_of_prep - писок препаратов
spis_of_date - список дат
prep - конкретный препарат
'''
spis = [st[:-1].split('#') for st in open('scientist.csv', 'r', encoding='UTF-8')]
list_of_prep = []
for elem in spis[1:]:
    name_of_prep = elem[1]
    if not name_of_prep in list_of_prep:
        list_of_prep.append(name_of_prep)
spis_of_date = []
for prep in list_of_prep:
    dat1 = date(5000,12,31)
    for elem in spis[1:]:
        year, mounth, day = [int(x) for x in elem[2].split('-')]
        dat = date(year, mounth, day) # здесь находится дата из списка ученых
        if prep == elem[1] and dat < dat1:
            dat1 = dat
    spis_of_date.append(dat1)

with open('scientist_origin.txt', 'w') as f2:
    print('#'.join(spis[0]), file=f2)     #запись в файл заголовка
    fin_sp = []    # список с натоящими учеными
    for elem in spis[1:]:
        year, mounth, day = [int(x) for x in elem[2].split('-')]
        dat2 = date(year, mounth, day)
        for i in range(len(list_of_prep)):
            if elem[1] == list_of_prep[i] and dat2 == spis_of_date[i]:
                fin_sp.append(elem)
    finish = sorted(fin_sp)   # сортировка
    for one in spis[1:]:
        print(one)
        print('#'.join(one), file=f2)      # запись в файл ученых
