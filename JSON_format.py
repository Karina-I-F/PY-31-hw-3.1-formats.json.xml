import json


def get_tag_content(file, tag):
    """
    Принимает JSON файл и тип тегов
    Возвращает список содержимого тегов данного типа
    """
    with open(file, encoding='utf-8') as datafile:
        json_data = json.load(datafile)
        data_list = []
        for data in json_data['rss']['channel']['items']:
            data_list.append(data[tag])
    return data_list


def word_counter(file, tag):
    """
    Принимает JSON файл и тег
    Выводит топ-10 слов длиннее 6 символов
    """
    data_list = get_tag_content(file, tag)
    reduplication = {}
    for phrase in data_list:
        words = phrase.split()
        for word in words:
            if len(word) > 6:
                reduplication[word.lower()] = reduplication.get(word.lower(), 0) + 1
    top = []
    for key, value in reduplication.items():
        top.append((value, key))
    top.sort(reverse=True)
    place = 1
    for item in top[0:10]:
        print(f'{place}. Слово "{item[1]}" встречается {item[0]} раз.')
        place += 1


word_counter('newsafr.json', 'description')
