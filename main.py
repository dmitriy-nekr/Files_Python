import pprint
import os

#Задание 1

def make_cook_book(file):
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            if len(line) > 2  and "|" not in line:
                key = line.strip()
                cook_book[key]=[]
            elif key in cook_book and "|" in line:
                composition = line.split("|")
                new_dict = {'ingredient_name':composition[0].strip(), 'quantity': int(composition[1].strip()), 'measure': composition[2].strip()}
                cook_book[key].append(new_dict)
    return cook_book
pprint.pprint(make_cook_book('recipes.txt'))


#Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    result={}
    cook_book = make_cook_book('recipes.txt')
    for dish in dishes:
        for ingredient_dict in cook_book[dish]:
            name = ingredient_dict['ingredient_name']
            if name in result:
                result[name]['quantity'] = result[name]['quantity'] + ingredient_dict[name]['quantity'] * person_count
            else:
                result[name] = { 'measure': ingredient_dict['measure'], 'quantity':(ingredient_dict['quantity'] * person_count)}
    return result


pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2))


#Задание 3
def create_file_dict(directory):
    file_dict = {}
    files = os.listdir(directory)
    for file in files:
        with open(directory + '/' + file, encoding='utf-8') as f:
            data = f.readlines()
            file_dict[file] = data

    return file_dict

def write_in_order(some_dict):
    sorted_dict = dict(sorted(some_dict.items(), key=lambda item: len(item[1])))
    for key, data in sorted_dict.items():
        with open('result.txt', "a") as f:
            f.write(key + '\n')
            f.write(str(len(sorted_dict[key])) + '\n')
            for string_ in sorted_dict[key]:
                f.write(string_ + '\n')

write_in_order(create_file_dict('./new'))
