# Документ «article.txt» содержит текст:
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

with open('article2.txt', 'w', encoding='utf-8') as data:
    text = ['Вечерело', 'Жужжали мухи', 'Светили фонарики', 'Кипела вода в чайнике', 'Венера зажглась на небе',
            'Деревья шумели']
    for words in text:
        data.write(str(words) + '\n')


def longest_words(file):
    with open(file, 'r', encoding='utf-8') as data:
        words = data.read().split()
        print(words)
        size = 1
        result = []
        for i in range(len(words)):
            if len(words[i]) == size:
                result.append(words[i])
            elif int(len(words[i])) > size:
                size = int(len(words[i]))
                result.clear()
                result.append(words[i])
        return result


print(longest_words('article2.txt'))
