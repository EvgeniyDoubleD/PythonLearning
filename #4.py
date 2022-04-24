#Показать первую цифру дробной части числа

number = float(input("vvedite drobnoe chislo"))
result = int((number*10)%10)
print(result)