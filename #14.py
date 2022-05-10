# Подсчитать сумму цифр в вещественном числе.

def try_parse():
    while True:
        try:
            dotA = int(input("Введите вещественное число: "))
            return abs(int(dotA))
        except ValueError:
            print("Не подходящее значение")


b = try_parse()
sum = 0
while b != 0:
    a = int(b % 10)
    sum = a+sum
    b = b/10

print(sum)
