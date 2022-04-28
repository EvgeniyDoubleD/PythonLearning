#Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

def try_parse_int():
    while True:
        try:
            console_input = int(input("Укажите кол-во членов последовательности: "))
            return int(console_input)
        except ValueError:
            print("Не подходящее значение")

N = try_parse_int()

for i in range (0,N):
    if i%2 == 0:
        i=3**i
    else:
        i=-3**i  
    print(i, end = ", ")