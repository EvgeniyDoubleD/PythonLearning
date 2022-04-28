#Найти расстояние между двумя точками пространства

import math

def try_parse():
    while True:
        try:
            dot = float(input("Координаты точки X: ")),float(input("Координаты точки Y: "))
            return tuple(dot)
        except ValueError:
            print("Не подходящее значение")
      
print("Введите координаты Х и У первой точки пространства ")            
dotA = try_parse()
print("Введите координаты Х и У второй точки пространства ")     
dotB = try_parse()

rangeBetween = math.sqrt((math.pow((dotB[0]-dotA[0]),2))+(math.pow((dotB[1]-dotA[1]),2)))

print(rangeBetween)