def add_everything_up(a, b):
    try:
        result = a + b
        return result

    except TypeError as exc:
        result = str(a) + str(b)
        return f'{result}, но была ошибка {exc}'




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
