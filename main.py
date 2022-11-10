with open("recipes.txt", "rt", encoding="utf-8") as file:
    cook_book = {}
    for l in file:
        dish = l.strip()
        count_ingredient = int(file.readline())
        ingredient_list = []
        for _ in range(count_ingredient):
            ingredient = file.readline().strip().split( "|" )
            ingredient_name, quantity, measure = ingredient
            ingredient_dict = {"Ингредиент" : ingredient_name,"Количество" : quantity, "Мера" : measure}
            ingredient_list.append(ingredient_dict)
        file.readline()
        cook_book[dish] = ingredient_list
    print(cook_book)
print("-----------------------")
def et_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for i in cook_book.keys():
        if i in dishes:
            for ingr in cook_book[i]:
                if ingr['Ингредиент'] not in ingredient_dict:
                    ingredient_dict[ingr['Ингредиент']] = {'Количество' : int(ingr['Количество']) * person_count, 'Мера' :ingr['Мера']}
                else:
                    ingredient_dict[ingr['Ингредиент']]['Количество'] += int(ingr['Количество']) * person_count
    print(ingredient_dict)

et_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print("--------------------------------------")

import os
files = os.listdir("folder")
file_str_list = []
file_dict = {}
for file_name in files:
    with open(f"folder/{file_name}", "rt", encoding="utf-8") as file1:
        count = 0
        for i in file1:
            count += 1
    file_str_list.append(count)
    file_dict[count] = file_name
# print(file_str_list)
# print(file_dict)
file_str_list.sort()
with open("file_sorted.txt", "wt", encoding="utf-8") as file2:
    str = ""
    for i in file_str_list:
        with open(f"folder/{file_dict[i]}", "rt", encoding="utf-8") as file3:
            str += f'{file_dict[i]}\n{file3.read()}\n\n'
    file2.write(str)
