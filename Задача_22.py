# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

arr_n = int(input('Введи размер первого массива: '))
arr_m = int(input('Введи размер второго массива: '))
import random
arr_n = [random.randint(0, 10) for i in range(arr_n)]
arr_m = [random.randint(0, 10) for i in range(arr_m)]
arr_1 = set(arr_n)
arr_2 = set(arr_m)
inters = arr_1.intersection(arr_2)
print(*arr_n, sep ='    ')
print(*arr_m, sep ='    ')
print(*sorted(inters), sep ='    ')