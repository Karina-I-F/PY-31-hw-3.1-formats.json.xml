import xml.etree.ElementTree as ET


def parse_xml_file(file):
    """
    Принимает XML файл
    Создаёт парсер
    Возвращает корень
    """
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file, parser)
    root = tree.getroot()
    return root


def get_tag_content(file, tag):
    """
    Принимает XML файл и тип тегов
    Возвращает список содержимого тегов данного типа
    """
    parsed_file = parse_xml_file(file)
    xml_items = parsed_file.findall('channel/item')
    data_list = []
    for data in xml_items:
        data_list.append(data.find(tag).text)
    return data_list


def word_counter(file, tag):
    """
    Принимает XML файл и тег
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


word_counter('newsafr.xml', 'description')
