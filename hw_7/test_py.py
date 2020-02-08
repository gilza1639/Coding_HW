import random

def randome_list_gen(long, hight):
    output_list = []
    for i in range(hight):
        in_list = []
        for j in range(long):
            in_list.append(random.randint(-100, 100))
        output_list.append(in_list)
    return output_list

print (randome_list_gen(5, 8))