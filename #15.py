#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

def try_parse():
    while True:
        try:
            dotA = int(input("Введите число: "))
            return abs(int(dotA))
        except ValueError:
            print("Не подходящее значение")


b = try_parse()
j = 1
for i in range (1,b+1):
    c = j*(i)
    j = c
    print(c)
