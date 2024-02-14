import csv
import time
import datetime

year_sum = 0
data_write = []
#открываем файл
with open('songs.csv', newline='', encoding='utf-8') as csvfile:
    #считываем файл
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')

    for row in spamreader:
        #первая строка названия столбиков мне было лень что-то придумывать поэтому это костыль, но иначе никак не убирать !!!
        try:
            year_sum = sum([int(i) for i in row[-1].split('.')])
        except: pass
        # сравниваю когда была выпущена песня простым сложением
        if year_sum >= 2004:
            #вычленяю информацию
            name_art = row[2]
            name_song = row[1]
            pros = row[0]
            if pros == '0':
                #считаю прослушивая когда 0
                date = row[-1].split('.')
                pros = int(abs((int(date[0])-1+(int(date[1])-1)*30+(int(date[2])-2002)*365)/(len(row[1])+len(row[2])))*10000)
            data_write.append([name_song,name_art,pros])
#записываю в таблицу
with open('songs_new.csv','w',newline='', encoding='utf-8') as file:
    write = csv.writer(file, delimiter=';', quotechar='|')

    for data in data_write:
        write.writerow(data)
    file.close()