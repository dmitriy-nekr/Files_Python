import pprint

#Задание 1
cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        if len(line) > 2  and "|" not in line:
            key = line.strip('\n')
            cook_book[key]=[]
        elif key in cook_book and "|" in line:
            composition = line.split("|")
            new_dict = {'ingredient_name': composition[0], 'quantity': composition[1], 'measure': composition[2].strip('\n')}
            cook_book[key].append(new_dict)

pprint.pprint(cook_book)


# #Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    result={}
    for dish in dishes:
        for ingredient_dict in cook_book[dish]:
            name = ingredient_dict['ingredient_name']
            if name in result:
                result[name]['quantity'] = int(result[name]['quantity']) + int(ingredient_dict[name]['quantity']) * person_count
            else:
                result[name] = { 'measure': ingredient_dict['measure'], 'quantity':(int(ingredient_dict['quantity']) * person_count)}
    return result


pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2))


#Задание 3
with open('1.txt', encoding='utf-8') as f:
    data0 = f.readlines()
with open('2.txt', encoding='utf-8') as f:
    data1 = f.readlines()
with open('3.txt', encoding='utf-8') as f:
    data2 = f.readlines()

name0 = '1.txt'
name1 = '2.txt'
name2 = '3.txt'

file_dict={name0:data0, name1:data1, name2:data2}
print(file_dict)
def write_in_result_file(name):
    with open('result.txt',"a") as f:
        f.write(name + '\n')
        f.write(str(len(file_dict[name])) + '\n')
        for string_ in file_dict[name]:
            f.write(string_ + '\n')


sorted_dict = dict(sorted(file_dict.items(), key=lambda item: len(item[1])))

for key, data in sorted_dict.items():
    write_in_result_file(key)

