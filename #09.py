#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

def try_parse_int():
    while True:
        try:
            console_input = int(input("Укажите номер четверти от 1 до 4: "))
            if console_input>=1 and console_input <=4:
                return int(console_input)
        except ValueError:
            print("Не подходящее значение")
            
quarter = try_parse_int()

if quarter == 1:
    print("Допустимые значения координат с точками х>0 y>0 ")
if quarter == 2:
    print("Допустимые значения координат с точками х<0 y>0 ")
if quarter == 3:
    print("Допустимые значения координат с точками х<0 y<0 ")
if quarter == 4:
    print("Допустимые значения координат с точками х>0 y<0 ")