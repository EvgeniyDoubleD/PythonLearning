#


dotA = input("Введите вещественное число: ")
if "." in dotA:
    Chunk = dotA.split('.')
    #print type(Chunk[0])
    p = len(Chunk)
    sum = ""
    for i in range(0,p):
        sum = sum + (str(Chunk[i]))
    print(sum)
    sum2 = int(sum)
    print(sum2)
    itog = 0
    while sum2 > 0:
        itog = (int(sum2)%10) + itog
        sum2 = sum2/10
    print(itog)
else:
        itog = 0
        while dotA > 0:
            itog = (int(dotA)%10) + itog
        sum2 = dotA/10
        print(itog)