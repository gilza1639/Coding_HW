'''
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().

 PS

 Текст взял с https://www.lipsum.com/
'''

my_list = ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting',
           'industry.', 'Lorem', 'Ipsum', 'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text', 'ever',
           'since', 'the', '1500s,', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and',
           'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book.', 'It', 'has', 'survived', 'not', 'only',
           'five', 'centuries,', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting,', 'remaining',
           'essentially', 'unchanged.', 'It', 'was', 'popularised', 'in', 'the', '1960s', 'with', 'the', 'release',
           'of', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages,', 'and', 'more', 'recently', 'with',
           'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'of', 'Lorem',
           'Ipsum.']
'''
 При решении ДЗ в начале урока вы сказали, что если рассчет используется несоклько раз, то следует создать переменную.
Поэтому вот:
'''
num = len(my_list)

final_list = my_list.copy()

for id, name in enumerate(my_list):
    if num%2==0 and id == num-1:
        break
    if id%2==1:
        final_list.pop(id)
        final_list.insert(id-1, name)
print (final_list)
print (my_list)
