# Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
# Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

with open("referat.txt", "r", encoding="utf-8") as referat:
    referat_symbols_count = 0
    referat_words_count = 0

    for line in referat:
        referat_symbols_count += len(line)
        referat_words_count += len(line.split())
        line = line.replace('.', '!')        
        with open('referat2.txt', 'a', encoding='utf-8') as referat2: 
            referat2.write(line)

    print(referat_symbols_count) # получилось 1509, а в notepad++ пишет, что 2823. Где верно?
    print(referat_words_count) # совпало с подсчетом в word
