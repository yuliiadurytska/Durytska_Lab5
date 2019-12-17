import statistics
import copy

users_data = open('Base.txt').readlines()

user_list = []

for user in users_data[1:]:
    user_list.append(user.split('\t'))

super_list = [[], [], [], [], []]

for user in user_list:
    for i in range(5):
        value = user[i + 1].strip()
        value = value.replace(',', '.')
        if value != 'N/A':
            super_list[i].append(float(value))

seredne_aryfmetychne_list = []
moda_list = []
mediana_list = []
normalizatsia_list = []

for column in super_list:
    seredne_aryfmetychne_list.append(statistics.mean(column))
    moda_list.append(statistics.mode(column))
    mediana_list.append(statistics.median(column))


print('Середні арифметичні по стовпцям')
print(seredne_aryfmetychne_list)
print('Моди по стовпцям')
print(moda_list)
print('Медіани по стовпцям')
print(mediana_list)

ser_ar_final_list = []
moda_final_list = []
mediana_final_list = []
inner_list1 = []
inner_list2 = []
inner_list3 = []

header = '\t'.join(['Cost($)', 'product_1(kg)', 'product_2(g)', 'product_3(quantity)', 'product_4(quantity'])

file1 = open('TabSA.txt', 'w')
file2 = open('TabMODA.txt', 'w')
file3 = open('TabMD.txt', 'w')
file1.writelines([header + '\n'])
file2.writelines([header + '\n'])
file3.writelines([header + '\n'])

for user_row in user_list:

    inner_list1.clear()
    inner_list2.clear()
    inner_list3.clear()

    for index, number in enumerate(user_row):
        number = number.strip()
        number = number.replace(',', '.')
        if number == 'N/A':
            inner_list1.append(str(round(seredne_aryfmetychne_list[index - 1], 2)))
            inner_list2.append(str(round(moda_list[index - 1], 2)))
            inner_list3.append(str(round(mediana_list[index - 1], 2)))
        else:
            inner_list1.append(number)
            inner_list2.append(number)
            inner_list3.append(number)
    file1.write("\t".join(inner_list1) + '\n')
    file2.write("\t".join(inner_list2) + '\n')
    file3.write("\t".join(inner_list3) + '\n')
    ser_ar_final_list.append(copy.deepcopy(inner_list1))
    moda_final_list.append(copy.deepcopy(inner_list2))
    mediana_final_list.append(copy.deepcopy(inner_list3))

file1.close()
file2.close()
file3.close()

first_col = []
second_col = []
third_col = []
forth_col = []
fifth_col = []

for user_row in ser_ar_final_list:
    first_col.append(float(user_row[1]))
    second_col.append(float(user_row[2]))
    third_col.append(float(user_row[3]))
    forth_col.append(float(user_row[4]))
    fifth_col.append(float(user_row[5]))

first_col_normalized = []
second_col_normalized = []
third_col_normalized = []
forth_col_normalized = []
fifth_col_normalized = []


for i in range(30):
    first_col_normalized.append((first_col[i] - min(first_col)) / (max(first_col) - min(first_col)))
    second_col_normalized.append((second_col[i] - min(second_col)) / (max(second_col) - min(second_col)))
    third_col_normalized.append((third_col[i] - min(third_col)) / (max(third_col) - min(third_col)))
    forth_col_normalized.append((forth_col[i] - min(forth_col)) / (max(forth_col) - min(forth_col)))
    fifth_col_normalized.append((fifth_col[i] - min(fifth_col)) / (max(fifth_col) - min(fifth_col)))

# print(first_col_normalized)

file_normalized = open('TabNorm.txt', 'w')
file_normalized.writelines([header + '\n'])


for i in range(30):
    line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(user_list[i][0],
                                             round(first_col_normalized[i], 2),
                                             round(second_col_normalized[i], 2),
                                             round(third_col_normalized[i], 2),
                                             round(forth_col_normalized[i], 2),
                                             round(fifth_col_normalized[i], 2))
    file_normalized.write(line)

file_normalized.close()
