# ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной
# данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
# Сколько минут на это потребуется?
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt
#
# Пример
# Ввод
#
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
#
# Вывод
# 32.72727272727273
import random

with open('pipes.txt', 'r', encoding='utf-8') as pipes:
    info = pipes.read().splitlines()
    pipe_time = []
    for i in range(len(info)):
        if info[i] == '':
            break
        pipe_time.append(float(info[i]))

    pipe_num = info[-1].split()
    pipe_num = [int(i) for i in pipe_num]


def calc_time(pipe, time_p):
    pipe_minut = list(map(lambda i: time_p[i - 1] * 60, pipe))
    max_time = max(pipe_minut)
    sum = 0
    for j in pipe_minut:
        sum += max_time / j
    return max_time / sum

with open('time.txt', 'w', encoding='utf-8') as time_result:
    time_result.write(f'Время заполнения бассейна трубами № {pipe_num} cоставит {calc_time(pipe_num, pipe_time)} минут')