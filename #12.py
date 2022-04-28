#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
def try_parse_int():
    while True:
        try:
            console_input = int(input("Введите N значений словаря: "))
            return int(console_input)
        except ValueError:
            print("Не подходящее значение")

N = try_parse_int()

dictIndex = {}
for i in range (1,N+1):
    dictIndex[i] = (3*i)+1
    
print(dictIndex)