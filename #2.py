# Найти максимальное из пяти чисел
import random
print("Сформировано 5 случайных чисел:")
numbers = list()
size = 5
i = 0
while i < size:
    a = random.randint(1, 99)
    numbers.append(a)
    i += 1
print(numbers)
print("Максимальное значение:")
print (max(numbers))
