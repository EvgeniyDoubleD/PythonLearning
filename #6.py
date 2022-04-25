
# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

def try_parse_int():
    while True:
        try:
            console_input = int(input("Введите день недели: "))
            if console_input>0 and console_input <=7:
                return int(console_input)
        except ValueError:
            print("Не подходящее значение")


day = try_parse_int()-1

weekdays = ["Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота", "Воскресенье"]

if weekdays[day] == 'Суббота':
    print(f"Выходной день недели - {weekdays[day]}")
elif weekdays[day] == 'Воскресенье':
    print(f"Выходной день недели - {weekdays[day]}")
else:
    print(f"Будний день недели - {weekdays[day]}")