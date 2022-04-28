# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def try_parse():
    while True:
        try:
            dotA = float(input("Координаты точки: "))
            return float(dotA)
        except ValueError:
            print("Не подходящее значение")


def get_quarter(x, y):
    if x > 0 and y > 0:
        print("Точка в первой четверти")
    if x > 0 and y < 0:
        print("Точка в четвертой четверти")
    if x < 0 and y > 0:
        print("Точка во второй четверти")
    if x < 0 and y < 0:
        print("Точка в третьей четверти")
    if x == 0 and y != 0:
        print("Точка на оси Y")
    if x != 0 and y == 0:
        print("Точка на оси Х")


print("Точка X")
a = try_parse()
print("Точка Y")
b = try_parse()
get_quarter(a, b)
