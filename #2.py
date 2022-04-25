# Найти максимальное из пяти чисел
import random
print("Сформировано 5 случайных чисел:")
numbers = list()
size = 5
i = 0
while i < size:
    a = random.randint(55, 199)
    numbers.append(a)
    i += 1
print(numbers)
max = numbers[0]
for k in numbers:
    if k > max:
        max = k
print("Максимальное значение:")
print (max)