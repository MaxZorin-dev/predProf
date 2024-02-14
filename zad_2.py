import csv

name_art = input("Имя артиста:")


#открываем файл
with open('songs.csv', newline='', encoding='utf-8') as csvfile:
    #считываем файл
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')

    for row in spamreader:
        if row[1] == name_art:
            print(f"У {name_art} найдена песня: {row[2]}")
            break