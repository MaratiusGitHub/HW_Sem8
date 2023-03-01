# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить
# на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано
# положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        if 1 < lines > len(text):
            print('Введено неверное количество строк')
        else:
            for i in range(len(text) - lines, len(text)):
                print(text[i])


line_num = int(input('Введите номер строки: '))
print(read_last(line_num, 'article.txt'))

