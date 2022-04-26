a1 = int(input("vvedite pervoe chislo"))
a2 = int(input("vvedite vtoroe chislo"))
if a2**2 == a1 or a2 == a1**2:
    print ("Kvadratom yavlaetsa")
else:
    print ("NET")
    
    weekdays = ["Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота", "Воскресенье"]

if weekdays[niceDay] == "Воскресенье" or "Суббота":
    print(f"Выходной день недели - {weekdays[niceDay]}")
else:
    print(f"Будний день недели - {weekdays[niceDay]}")