#Попросить пользователя ввести возраст при помощи input и положить результат в переменную
#Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
#Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в преременную
#Вывести содержимое переменной на экран


def input_of_age():
    age = 0
    age = (input('Type your age, please:'))
    return age

def age_classificator(age):
    age = int(age)
    if   age < 7:
        age_category = 'Детсад'
    elif age >= 7 and age <= 18:
        age_category = 'Школа'
    elif age >= 19 and age <= 24:
        age_category = 'ВУЗ'
    elif age >= 25 and age <= 65:
        age_category = 'Работа'
    else:
        age_category = 'Пенсия'
    print(age_category)

age_classificator(input_of_age())