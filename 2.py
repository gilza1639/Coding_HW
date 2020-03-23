'''
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().

'''
# чтоб с input().split() не париться сразу сгенерировал список
# и чтобы десять раз не копировать код сделал в виде функции. скоро мы ее должны пройти)


def IndexChanger(my_list):
    print('\n' + '='*20 + 'Start' + '='*20 + '\n')
    print(f'Original -\t {my_list}')
    for i in range(len(my_list) // 2):
        my_list[i * 2:2 + i * 2] = my_list[1 + 2 * i], my_list[2 * i]
    print(f'Edited -\t {my_list}')
    print('\n' + '=' * 20 + 'End' + '=' * 20 + '\n')


test_even = [el for el in range(1, 51)]
test_odd = [el for el in range(1, 50)]
test_word = 'Hello dear friends im from Mexico and im bring cocaine'.split()

IndexChanger(test_even)
IndexChanger(test_odd)
IndexChanger(test_word)