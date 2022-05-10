#Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

def try_parse():
    while True:
        try:
            dotA = int(input("Введите число: "))
            return abs(int(dotA))
        except ValueError:
            print("Не подходящее значение")


b = try_parse()

ran = []

for i in range(1,b+1):
    ran.append(1+(1/i)**i)
print('Сформирован массив: ')
for j in ran:
    k = round(j,3)
    print(k, end = " ")
print()
print(f'Сумма чисел последовательности: {sum(ran):.3f}')