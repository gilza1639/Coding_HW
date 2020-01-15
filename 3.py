"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
 Считаем 3 + 33 + 333 = 369.
"""
str_num = str(input('Введите число n, чтобы найти сумму n + nn + nnn \n   Число: '))
int_num = (int(str_num * 3) + int(str_num * 2) + int(str_num))
print(int_num)

# 2 вариант

print(int(str_num) * 123)
