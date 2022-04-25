#Показать первую цифру дробной части числа

number = float(input("Введите дробное число: "))
result = int((number*10)%10)
print(result)