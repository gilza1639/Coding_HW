'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
with open('5_py.txt', "w+", encoding='utf-8') as f_obj:
    while True:
        try:
            string = [int(el) for el in input('введите числа через пробел ( или сторонний символ для выхода): ').split()]
        except ValueError:
            f_obj.seek(0)
            count = [int(el) for el in f_obj.readline().split()]
            print('Сумма введенных чисел', sum(count))
            break
        print (string)
        for el in string:
            print(f'{str(el)}', file=f_obj, end=' ')
        # считаем
