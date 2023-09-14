def celsius_fahrenheit(c):
    formula = (C * 9/5) + 32
    return f"El resultado es {formula}"


def celsius_kelvin(C):
    formula = C + 273.15
    return f"El resultado es {formula}"


if __name__ == '__main__':
    C = 10
    print(celsius_fahrenheit(C))
    print(celsius_kelvin(C))
    