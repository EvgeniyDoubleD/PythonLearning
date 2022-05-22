# Подсчитать сумму цифр в вещественном числе.

dotA = input("Введите вещественное число: ")
if "." in dotA:
    Chunk = dotA.split('.')
    # print type(Chunk[0])
    p = len(Chunk)
    sum = ""
    for i in range(0, p):
        sum = sum + (str(Chunk[i]))
    # print(sum)
    sum2 = int(sum)
    # print(sum2)
    itog = 0
    while sum2 > 0:
        itog = (int(sum2) % 10) + itog
        sum2 = sum2/10
    print(itog)
else:
    dotB = int(dotA)
    print(type(dotB))
    itog = 0
    while int(dotB) > 0:
        itog = (dotB % 10) + itog
        dotB = dotB/10
    itog2 = int(itog)
    print(type(itog2))
    print(itog2)
