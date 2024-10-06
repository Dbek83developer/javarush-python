# Зона видимости переменной.

# Исправьте код, чтобы последний print выводил исключение.

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)


def bad():
    exc = None
    try:
        bar(1)
    except KeyError as e:
        exc = e
        print('key error')
    except ValueError as e:
        exc = e
        print('value error')

    print(exc)  # This should raise an exception because e is not defined in this scope


bad()
