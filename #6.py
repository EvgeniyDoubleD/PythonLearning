from re import S


def try_parse_int():
    while True:
        try:
            console_input = int(input("Enter a weekday number: "))
            if console_input > 0:
                return int(console_input)
        except ValueError:
            print("Is not a valid number.")


a = try_parse_int()
print(a)
