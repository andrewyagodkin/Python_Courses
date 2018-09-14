#Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало

def get_summ(num_one, num_two):
    try:
        first = int(num_one)
        second = int(num_two)
        num_sum= first + second
        return num_sum
    except(ValueError):
        return 'Ошибка приведения типов'
def main():
    temp1=input('Ввод первого числа: ')
    temp2=input('Ввод второго числа: ')
    print('Сумма чисел:'+ str(get_summ(temp1, temp2)))
    main()

main()


