'''

3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

'''

# 1 вариант

my_list = [12, "winter", 1, "winter", 2, "winter",
           3, "spring", 4, "spring", 5, "spring",
           6, "summer", 7, "summer", 8, "summer",
           9, "autumn", 10, "autumn", 11, "autumn"]
while True:
    season = 0
    print('--v1--\nВведите число от 1 до 12')
    season = int(input())
    if 1 <= season <= 12:
        break
print(my_list[my_list.index(season) + 1])

# 2 вариант

season_list = ["winter", "winter", "spring", "spring", "spring",
               "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
season_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while True:
    season = 0
    print('--v2--\nВведите число от 1 до 12')
    season = int(input())
    if 1 <= season <= 12:
        break
print(season_list[season_num_list.index(season)])

# 3 вариант

season_list = ["winter", "spring", "summer", "autumn"]
while True:
    season = 0
    print('--v3--\nВведите число от 1 до 12')
    season = int(input())
    if 1 <= season <= 12:
        break

if season == 3 or season == 4 or season == 5:
    print("spring")
elif season == 6 or season == 7 or season == 8:
    print("summer")
elif season == 9 or season == 10 or season == 11:
    print("autumn")
elif season == 12 or season == 1 or season == 2:
    print("winter")

'''

Вопрос к преподавателю!

изначально хотел сделать что-то типа

seasons_list = [[12, 1, 2, "winter"], [3, 4, 5, "spring"], [6, 7, 8, "summer"], [9, 10, 11, "autumn"]]

Но как из этого найти в каком из листов в главном листе находится мое число?
Узнав индекс листа можно потом внутри него по идексу -1 либо 3 вывести сезон

Как сделать это без перебора? Ибо если будет 100к подобных листов перебор займет кучу времени

'''

# через dict

seson_dict = {
    'summer': [6, 7, 8],
    'winter': [12, 1, 2],
    'autumn': [9, 10, 11],
    'spring': [3, 4, 5]
}

while True:
    season = 0
    print('----------dict---------- \n   Введите число от 1 до 12')
    season = int(input())
    if 1 <= season <= 12:
        break

for k, v in seson_dict.items():
    if season in v:
        print(k)
        break
