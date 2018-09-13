#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то что переданно функции строками. Если нет - вернуть 0
#Если строки одинаковые, верунть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты




from sys import stdin, exit as sys_exit  

def str_input():
    typedstring = input('Ввод строки: ')
    if typedstring == 'exit':
        sys_exit()
    else:
        return(typedstring)


def check_str(typedstring1, typedstring2):
    string1=typedstring1
    string2=typedstring2
    if isinstance(string1, str) and isinstance(string2, str):
        if string1 == string2:
            return 1
        elif len(string1) > len(string2):
            return 2
        elif string2 == 'learn':
            return 3

    else:return 0

def run():
    print('Введите строки для сравнения ниже, или "exit" для выхода из программы')
    print(check_str(str_input(),str_input()))
    run()
run()

