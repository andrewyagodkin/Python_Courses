#Оценки
#Создать список с оценками учеников разных классов школы вида
#[{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...] - список словарей
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

import random



def  list_gen(number_of_classes, number_of_marks):
    for i in range(0, number_of_classes):
        for j in ['а','б','в','г','д']:
            class_name = str(i)+str(j)
            marks_of_class = marks(number_of_marks)
            dictionary['class'] = class_name
            dictionary['marks_of_class'] = marks_of_class
            list_of_dicts.append(dictionary)
    return list_of_dicts

def marks(number_of_marks):
    for i in range(0, number_of_marks):
        marks_array.append(random.randrage(2,5,1))
    return marks_array

def  avg(data_list, number_of_classes, number_of_marks):
    print('Средние значения:\n')
    for i in range(1, (number_of_classes*5)):
        avg_class = sum(data_list[i['marks_of_class']]) / len(data_list[i['marks_of_class']])
        print ('В классе '+data_list[i['class']]+'средняя оценка по классу: '+avg_class)
        sum_school = sum_school + sum(data_list[i['marks_of_class']])
        number_school = number_school + len(data_list[i['marks_of_class']])
    school_avg = sum_school / number_school 
    print('Средняя оценка по школе:'+school_avg)


def common():

    classes_count = int(input('Количество классов:'))
    scores_count  = int(input('Количество оценок:'))
    avg_scores(list_gen(classes_count, scores_count),classes_count,scores_count)