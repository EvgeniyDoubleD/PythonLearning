#вывести числа от -н до н
import math
num = int(input("Введите число N: "))
absNum = abs(num)
print('Список от -N до N: ')
for i in range(-absNum, absNum+1):
    print(i, end= ' ')