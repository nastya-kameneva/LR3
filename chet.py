def divide(a,b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a/b

def is_even(number):
    return number % 2 == 0
